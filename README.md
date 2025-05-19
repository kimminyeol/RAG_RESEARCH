# Advanced RAG 연구 공간  
_RAG 기반 추천 시스템을 심화 학습하고 실험한 공간입니다._

---

## ✅ 소개

이 레포지토리는 **Retrieval-Augmented Generation (RAG)** 기반 추천 시스템을 연구하며 구축한 **개인 학습 및 실험 공간**입니다.  
기본적인 RAG 기술을 넘어, **그래프 기반 강화**, **사용자 선호 분석**, **실험 기반 최적화**를 목표로 다양한 시도를 진행했습니다.

특히, [NirDiamant/RAG_TECHNIQUES](https://github.com/NirDiamant/RAG_TECHNIQUES)와 같은 공개 RAG 자료를 참고하며  
**실제 추천 시스템에 적용 가능한 고급 RAG 파이프라인**을 구현하는 것을 목표로 했습니다.

---

## 📂 폴더 구조
Advanced_RAG/
│
├── RAG_deepai/        
├── RAG_tech/          # 다양한 Advanced_RAG skill 저장소
├── data/              
├── evaluation/        
├── images/            
├── tests/             
├── vector_stores/     
├── helper_functions.py
├── requirements.txt   
│
└── RAG_Rec/           # RAG-based Recommender System 실험공간-> 정리중.
    ├── data/              
    ├── Graph_Embedding_RGCN.ipynb      # Graph-based embedding exploration
    ├── RAG_ex_with_raptor.ipynb        # RAPTOR-based retrieval experiments
    ----


---

## 🚩 주요 학습 내용

1. **RAG 이론부터 실전까지**
   - 단순 검색부터 그래프 기반 검색까지 다양한 기술 실험
   - 검색 성능 평가 및 개선 방법 탐색

2. **실험 중심 개발**
   - Raptor
   - Context chunk header
   - GNN 

3. **추천 시스템 설계**
   - 사용자 선호 기반 추천 로직 설계
   - 벡터 저장소 관리 및 동적 쿼리 처리 실험

---
## 📌 Advanced RAG Techniques Overview

아래는 제가 학습하고 참고한 고급 RAG 기법들을 정리한 표입니다.

## 📌 Advanced RAG Techniques Overview

| #  | 카테고리           | 기법명                                         | 링크                                                                                                                         |
|----|--------------------|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| 1  | 기초 🌱            | Simple RAG                                    | [링크](https://github.com/kimminyeol/RAG_RESEARCH/blob/main/Advanced_RAG/RAG_tech/01_simple_rag.ipynb)                       |
| 2  | 기초 🌱            | Simple RAG with CSV                           | [링크](https://github.com/kimminyeol/RAG_RESEARCH/blob/main/Advanced_RAG/RAG_tech/02_simple_csv_rag.ipynb)                   |
| 3  | 기초 🌱            | Reliable RAG                                  | [링크](https://github.com/kimminyeol/RAG_RESEARCH/blob/main/Advanced_RAG/RAG_tech/03_reliable_rag.ipynb)                     |
| 4  | 쿵크 사이즈 최적화 📏 | Choose Chunk Size                              | [링크](https://github.com/kimminyeol/RAG_RESEARCH/blob/main/Advanced_RAG/RAG_tech/04_choose_chunk_size.ipynb)                |
| 5  | 문장 단위 청킹 ⛓️  | Proposition Chunking                          | [링크](https://github.com/kimminyeol/RAG_RESEARCH/blob/main/Advanced_RAG/RAG_tech/05_proposition_chunking.ipynb)             |
| 6  | 쿼리 확장 🔍       | Query Transformations                         | [링크](https://github.com/kimminyeol/RAG_RESEARCH/blob/main/Advanced_RAG/RAG_tech/06_query_transformations.ipynb)            |
| 7  | 가설 쿼리 생성    | HyDE (Hypothetical Document Embedding)        | [링크](https://github.com/kimminyeol/RAG_RESEARCH/blob/main/Advanced_RAG/RAG_tech/07_HyDe_Hypothetical_Document_Embedding.ipynb) |
| 8  | 문맥 강화        | Contextual Chunk Headers                      | [링크](https://github.com/kimminyeol/RAG_RESEARCH/blob/main/Advanced_RAG/RAG_tech/08_contextual_chunk_headers.ipynb)         |
| 9  | 문맥 강화        | Relevant Segment Extraction                   | [링크](https://github.com/kimminyeol/RAG_RESEARCH/blob/main/Advanced_RAG/RAG_tech/09_relevant_segment_extraction.ipynb)      |
| 10 | 문맥 강화        | Context Enrichment (Window Around Chunk)      | [링크](https://github.com/kimminyeol/RAG_RESEARCH/blob/main/Advanced_RAG/RAG_tech/10_context_enrichment_window_around_chunk.ipynb) |
| 11 | 문맥 강화        | Semantic Chunking                             | [링크](https://github.com/kimminyeol/RAG_RESEARCH/blob/main/Advanced_RAG/RAG_tech/11_semantic_chunking.ipynb)                |
| 12 | 문맥 압축        | Contextual Compression                        | [링크](https://github.com/kimminyeol/RAG_RESEARCH/blob/main/Advanced_RAG/RAG_tech/12_contextual_compression.ipynb)           |
| 13 | 문서 확장        | Document Augmentation                         | [링크](https://github.com/kimminyeol/RAG_RESEARCH/blob/main/Advanced_RAG/RAG_tech/13_document_augmentation.ipynb)            |
| 14 | 다중 소스 검색   | Fusion Retrieval                              | [링크](https://github.com/kimminyeol/RAG_RESEARCH/blob/main/Advanced_RAG/RAG_tech/14_fusion_retrieval.ipynb)                 |
| 15 | 재정렬           | Reranking                                     | [링크](https://github.com/kimminyeol/RAG_RESEARCH/blob/main/Advanced_RAG/RAG_tech/15_reranking.ipynb)                       |
| 16 | 계층적 색인      | Hierarchical Indices                           | [링크](https://github.com/kimminyeol/RAG_RESEARCH/blob/main/Advanced_RAG/RAG_tech/16_hierarchical_indices.ipynb)             |
| 17 | 멀티모달        | Multi-Modal RAG with Captioning                | [링크](https://github.com/kimminyeol/RAG_RESEARCH/blob/main/Advanced_RAG/RAG_tech/17_multi_model_rag_with_captioning.ipynb)  |
| 18 | 반복 검색        | Retrieval with Feedback Loop                  | [링크](https://github.com/kimminyeol/RAG_RESEARCH/blob/main/Advanced_RAG/RAG_tech/18_***_retrieval_with_feedback_loop.ipynb) |
| 19 | 설명 가능성      | Explainable Retrieval                         | [링크](https://github.com/kimminyeol/RAG_RESEARCH/blob/main/Advanced_RAG/RAG_tech/19_explainable_retrieval.ipynb)            |
| 20 | 적응형 검색      | Adaptive Retrieval                            | [링크](https://github.com/kimminyeol/RAG_RESEARCH/blob/main/Advanced_RAG/RAG_tech/20_adaptive_retrieval.ipynb)               |




