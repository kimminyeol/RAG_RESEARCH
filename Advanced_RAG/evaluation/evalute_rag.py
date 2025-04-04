"""
RAG Evaluation Script

This script evaluates the performance of a Retrieval-Augmented Generation (RAG) system
using various metrics from the deepeval library.

Dependencies:
- deepeval
- langchain_openai
- json

Custom modules:
- helper_functions (for RAG-specific operations)
"""
from dotenv import load_dotenv
import os
load_dotenv() 
import json
from typing import List, Tuple
from deepeval import evaluate
from deepeval.metrics import GEval, FaithfulnessMetric, ContextualRelevancyMetric
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from langchain_openai import ChatOpenAI
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from helper_functions import (
    create_question_answer_from_context_chain,
    answer_question_from_context,
    retrieve_context_per_question
)

# 평가를 위한 테스트 케이스 생성-> 질문, 정답, 생성된 답변, 검색된 문서를 맵핑
def create_deep_eval_test_cases(
    questions: List[str],
    gt_answers: List[str],
    generated_answers: List[str],
    retrieved_documents: List[str]
) -> List[LLMTestCase]:
    return [
        LLMTestCase(
            input=question,
            expected_output=gt_answer,
            actual_output=generated_answer,
            retrieval_context=retrieved_document
        )
        for question, gt_answer, generated_answer, retrieved_document in zip(
            questions, gt_answers, generated_answers, retrieved_documents
        )
    ]

# 정확성: 생성된 답변이 실제 정답과 얼마나 일치하는지? 
correctness_metric = GEval(
    name="Correctness",
    model="gpt-4o",
    evaluation_params=[
        LLMTestCaseParams.EXPECTED_OUTPUT,
        LLMTestCaseParams.ACTUAL_OUTPUT
    ],
    evaluation_steps=[
        "Determine whether the actual output is factually correct based on the expected output."
    ],
)

# 생성된 답변이 검색된 문서의 정보와 얼마나 신뢰성 있게 일치하는지 
faithfulness_metric = FaithfulnessMetric(
    threshold=0.7,
    model="gpt-4",
    include_reason=False
)

# 검색된 문서와의 관련성을 바탕으로 응답이 질문과 문맥적으로 얼마나 관련 있는지 평가 
relevance_metric = ContextualRelevancyMetric(
    threshold=1,
    model="gpt-4",
    include_reason=True
)

# 퍙가 함수
def evaluate_rag(chunks_query_retriever, num_questions: int = 5) -> None:
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o", max_tokens=2000)
    question_answer_from_context_chain = create_question_answer_from_context_chain(llm)

    # json 파일에서 질문과 정답 데이터 가져오기
    q_a_file_name = "../data/q_a.json"
    with open(q_a_file_name, "r", encoding="utf-8") as json_file:
        q_a = json.load(json_file)

    # 질문, 정답, 생성된 답변, 검색된 문서를 저장할 리스트 생성
    questions = [qa["question"] for qa in q_a][:num_questions]
    ground_truth_answers = [qa["answer"] for qa in q_a][:num_questions]
    generated_answers = []
    retrieved_documents = []

    # 질문에 대한 문맥 검색
    for question in questions:
        context = retrieve_context_per_question(question, chunks_query_retriever)
        retrieved_documents.append(context)
        context_string = " ".join(context)
        result = answer_question_from_context(question, context_string, question_answer_from_context_chain)
        generated_answers.append(result["answer"])

    # 평가를 위한 테스트 케이스 생성
    test_cases = create_deep_eval_test_cases(questions, ground_truth_answers, generated_answers, retrieved_documents)
    evaluate(
        test_cases=test_cases,
        metrics=[correctness_metric, faithfulness_metric, relevance_metric]
    )

if __name__ == "__main__":
    # Add any necessary setup or configuration here
    # Example: evaluate_rag(your_chunks_query_retriever_function)
    pass
