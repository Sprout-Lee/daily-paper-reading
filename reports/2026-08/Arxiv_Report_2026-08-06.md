# Arxiv Daily Deep Report - 2026-08-06

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 2
---

## 1. Teaching Nemotron Greek: Mining a Corpus, Adapting Retrieval, and Grounding Generation for Modern Greek across Specialist Domains

**作者**: Ayoub Kirouane, Christos Petrocheilos
**链接**: [2608.05138](https://arxiv.org/abs/2608.05138)
**分类**: Retrieval-Augmented Generation | **关键词**: Greek NLP, Retrieval-Augmented Generation, Dense Retrieval, BM25, Multilingual Embedding, Fine-tuning, MoE, LoRA, HERA Benchmark, Nemotron

## 核心痛点
- 现代希腊语在NVIDIA Nemotron检索模型和主要多语言检索基准（BEIR、MIRACL）中缺失，导致多语言密集检索对希腊语失效。
- 希腊语专家领域（法律、能源、金融、临床）的文档长且术语密集，需要RAG支持。
- 没有原生的高质量希腊语指令数据，必须依赖翻译，引入translationese风险。

## 方法创新
- 端到端适应Nemotron家族：挖掘语料、训练检索栈、合成阅读器监督、构建基准。
- **语料挖掘**：从407,053原始对清洗到65,773查询记录，采用positive-wins、合成查询控制（few-shot风格匹配、grounding规则、难度变化）、负例挖掘（Qwen3-Embedding-8B，余弦kNN窗口）。
- **阅读器监督**：合成40k示例，教师Sophea-Titan-1生成带引用的答案，通过随机黄金位置、可变负例数量、弃权目标设计鲁棒性。
- **HERA基准**：构建4,946项希腊语长检索基准，包含不可回答和多跳问题，有L1-L5难度阶梯。

## 实验结果
- BM25在所有五个领域超出现成的多语言嵌入器（包括8B），尽管无学习参数。
- 微调1B嵌入器在65,773对上将nDCG@10从0.362升至0.835，在通用希腊语上相对未适应模型+0.399，但相对BM25的优势不能泛化。
- 交叉编码器适应后成为可靠增益。
- LoRA微调30B-A3B MoE阅读器将答案正确性从29.4%提升到66.9%。
- 报告了四个评估陷阱，包括两个未复现的声明。

## 一句话评价
该论文通过完整的、可复现的数据构建和模型适应流程，展示了希腊语RAG的可行性，并揭示了合成数据、翻译数据和评估基准中的关键陷阱，为低资源语言RAG提供了重要参考。

---

## 2. Helping Music Co-Creation Agents 'Listen' Well: Hierarchical Self-Supervised World Models for Understanding and Generation

**作者**: Scott H. Hawley
**链接**: [2608.04378](https://arxiv.org/abs/2608.04378)
**分类**: Symbolic Music Understanding and Generation | **关键词**: self-supervised learning, world model, music co-creation, JEPA, Swin Transformer, representation learning, symbolic music, flow matching

### 核心痛点
音乐协作智能体需要内部表示既能支持理解又能支持生成，同时保持人类在创作流程中的主导权。现有生成模型隐式编码音乐结构但无法清晰表述；描述（理解）与再现（生成）对表示的要求不同，传统方法将两者视为权衡关系。

### 方法创新
提出层次化自监督世界模型（MIDI-RAE-JEPA-SON, MRJS），采用2.55M参数的Swin V2编码器，在MIDI钢琴卷帘图像上训练，使用JEPA风格目标：音高/时间平移等变性、掩码嵌入预测、分布正则化（SIGReg）及软因子分解损失，无需标签和音乐理论词汇。遵循表示自编码器（RAE）范式，将条件流匹配模型作为生成器，在像素空间从PCA降维的条件中生成音乐。同一编码器可同时用于感知（冻结嵌入）和生成（条件控制），并通过跨层级条件丢弃实现图形化提示（如掩码修复）而无需专门采样器。

### 实验结果
冻结嵌入的探测显示：音乐属性可解码的层级与其时间尺度相关（短语边界在粗粒度层，音符密度和和声细节在细粒度层）。加入小型和弦监督头后，联合和弦恢复率从0.18提升至0.54，键检测（从未监督）从0.16提升至0.70。像素级F1达到0.996，CPU推理2.8秒，Apple MPS上0.6秒，支持实时交互演示。

### 一句话评价
该工作为音乐共创智能体提供了高效、可控且保留人类代理权的层次化表示学习与生成框架，验证了自监督世界模型在符号音乐领域的强大潜力。

---

