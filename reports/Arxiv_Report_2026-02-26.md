# Arxiv Daily Deep Report - 2026-02-26

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 5
---

## 1. TG-ASR: Translation-Guided Learning with Parallel Gated Cross Attention for Low-Resource Automatic Speech Recognition

**作者**: Cheng-Yeh Yang, Chien-Chun Wang, Li-Wei Chen, Hung-Shin Lee, Hsin-Min Wang, Berlin Chen
**链接**: [2602.22039](https://arxiv.org/abs/2602.22039)
**分类**: Speech Recognition | **关键词**: Low-resource automatic speech recognition, Taiwanese Hokkien, translation-guided learning, parallel gated cross attention, multilingual auxiliary language integration

**核心痛点**：低资源自动语音识别（ASR）面临数据稀缺的挑战，特别是在台湾闽南语等语言中，虽然有大量口语内容（如电视剧），但转录数据有限，且字幕通常只有普通话，导致ASR系统性能不佳，影响语言保存和媒体可访问性。

**方法创新**：提出了TG-ASR框架，引入并行门控交叉注意力（PGCA）机制，该机制自适应地整合来自多语言翻译的嵌入（如通过多语言BERT生成）到Whisper ASR解码器中，以增强跨语言语义指导，同时确保训练稳定性和最小化语言间干扰。方法包括两阶段训练：先微调Whisper，再冻结部分参数并更新PGCA层。

**实验结果**：基于新构建的YT-THDC语料库（30小时台湾闽南语电视剧语音，带有对齐普通话字幕和手动验证转录），实验表明该方法实现了14.77%的相对字符错误率降低，有效提升了低资源ASR性能，并识别出最能增强性能的辅助语言。

**一句话评价**：这项研究创新地利用翻译引导学习解决低资源ASR问题，具有实用价值，能促进语言多样性和技术包容性。

---

## 2. A Knowledge-Driven Approach to Music Segmentation, Music Source Separation and Cinematic Audio Source Separation

**作者**: Chun-wei Ho, Sabato Marco Siniscalchi, Kai Li, Chin-Hui Lee
**链接**: [2602.21476](https://arxiv.org/abs/2602.21476)
**分类**: Audio Source Separation | **关键词**: Music Segmentation, Music Source Separation, Cinematic Audio Source Separation, Sound Demixing, HMM

**核心痛点**
传统音频分割和源分离方法依赖大量标注数据，如预分割的训练数据，这在现实场景中往往稀缺或不可得，限制了模型的训练和应用。特别是在音乐和电影音频中，缺乏单乐器段或结构化知识（如乐谱）导致分割和分离精度低。

**方法创新**
提出一种知识驱动的框架，利用外部知识源（如乐谱）结合隐马尔可夫模型（HMM）进行音频分割。该方法不依赖任何预分割的标注数据，直接从输入音频和相关知识自主学习构建模型。应用包括音乐分割、音乐源分离（MSS）和电影音频源分离（CASS），其中知识（如声音类别活动指示）被投影并融入分离器输入，以改善分离性能。

**实验结果**
在模拟数据集Slakh2100上，乐谱引导的学习在音乐分割和分离任务中表现优异。在电影音频源分离任务中，使用DnR数据集，该方法在DnR-nonverbal数据集上达到了state-of-the-art性能，优于纯数据驱动技术（如Demucs和BSRNN）。实验表明，知识驱动方法在无标注数据场景下有效提升了分割和分离的准确性。

**一句话评价**
该研究提出了一种创新的无监督知识驱动方法，有效利用外部知识解决音频分割和分离中标注数据稀缺的挑战，具有广泛的应用潜力。

---

## 3. iMiGUE-Speech: A Spontaneous Speech Dataset for Affective Analysis

**作者**: Sofoklis Kakouros, Fang Kang, Haoyu Chen
**链接**: [2602.21464](https://arxiv.org/abs/2602.21464)
**分类**: Speech Emotion Recognition | **关键词**: spontaneous speech, affective analysis, speech emotion recognition, dataset

## 核心痛点
现有情感语音数据集多依赖演绎或实验室诱导的情感，难以反映真实情境中的自发情感表达，导致模型在自然场景中的泛化能力受限。

## 方法创新
提出iMiGUE-Speech数据集，扩展自iMiGUE视频数据集，专注于自发语音情感分析。数据集基于真实网球大满贯赛后采访音频，捕获运动员在胜负后的自然情感。创新点包括：添加语音转录（使用Whisper Large）、说话者角色分离（采访者与受访者）、词级强制对齐（使用Montreal Forced Aligner），并通过自动处理流程（如pyannote.audio进行说话者日记化）提取元数据。数据集可同步配对原始iMiGUE的微手势注释，形成多模态资源。

## 实验结果
论文引入两个评估任务以建立初始基准：语音情感识别（SER）和基于转录的情感分析。这些任务利用预训练表示评估数据集在声学和语言模态中捕获自发情感状态的能力。具体性能数据在截断部分未提供，但强调了数据集对自发情感分析的实用性。

## 一句话评价
iMiGUE-Speech填补了自发情感语音数据的空白，为多模态情感分析和真实场景下的语音研究提供了宝贵资源。

---

## 4. MIDI-Informed Singing Accompaniment Generation in a Compositional Song Pipeline

**作者**: Fang-Duo Tsai, Yi-An Lai, Fei-Yueh Chen, Hsueh-Wei Fu, Li Chai, Wei-Jaw Lee, Hao-Chung Cheng, Yi-Hsuan Yang
**链接**: [2602.22029](https://arxiv.org/abs/2602.22029)
**分类**: Music Generation | **关键词**: MIDI-informed, Singing Accompaniment Generation, Compositional Pipeline, Song Generation, Music Synthesis

# 详细总结

## 核心痛点
传统端到端歌曲生成模型存在数据密集、计算密集、可编辑性有限的问题；而现有compositional方法中组件独立使用常导致节奏不齐、和谐漂移和间歇性歌声处理困难，缺乏系统基准和组件协同设计。

## 方法创新
提出MIDI-informed singing accompaniment generation (MIDI-SAG)，利用符号vocal MIDI分数作为条件信号，结合melody harmonization模块生成和弦进行，以改善节奏和和谐对齐；通过显式节奏/和谐控制与潜在扩散的音频延续能力，处理间歇性歌声并确保结构完整性；构建模块化compositional管道，包括melody composition、SVS和MIDI-SAG，使用轻量级训练组件降低资源需求。

## 实验结果
在单个RTX 3090 GPU上训练，仅需2.5k小时音频数据，在多个感知质量指标上接近开源端到端基线；提供音频演示并计划开源模型、代码和数据集元数据。

## 一句话评价
该工作通过MIDI-informed方法有效解决了compositional歌曲生成中的对齐和结构完整性问题，以较低计算成本实现了高质量、可编辑的歌曲输出。

---

## 5. EmoOmni: Bridging Emotional Understanding and Expression in Omni-Modal LLMs

**作者**: Wenjie Tian, Zhixian Zhao, Jingbin Hu, Huakang Chen, Haohe Liu, Binshen Mu, Lei Xie
**链接**: [2602.21900](https://arxiv.org/abs/2602.21900)
**分类**: Multimodal Emotional Dialogue | **关键词**: EmoOmni, Emotional Chain-of-Thought, Multimodal Emotional Dialogue, Perception-Reasoning-Expression, EmoOmniPipe

# 详细总结

## 核心痛点
现有Omni-Modal Large Language Models (Omni-LLMs) 在处理复杂现实场景时，表现出肤浅理解和情感响应不匹配的问题。主要问题包括：音频和视觉线索可能复杂、隐式或冲突；Thinker-Talker架构通过隐藏状态隐式连接，导致情感细节丢失；数据稀缺，缺乏真实世界、细粒度注释的多模态对话数据；评估方法有限，忽略情感智能的上下文对齐。

## 方法创新
- **框架**：提出EmoOmni，一个统一框架，模拟人类情感认知的Perception–Reasoning–Expression因果链，显式解耦情感理解、战略决策和声学表达。
- **方法**：引入Emotional Chain-of-Thought (E-CoT)，作为从细粒度多模态感知到文本响应的推理过程，并作为高级情感指令指导EmoOmni-Talker，确保语义和情感对齐。
- **数据与基准**：构建EmoOmniPipe数据管道，从电影和电视剧中提取和注释情感丰富的对话数据；建立EmoOmniEval基准，系统评估多模态情感对话任务的能力。
- **训练策略**：采用两阶段训练，逐步培养感知和推理能力。

## 实验结果
EmoOmni-7B模型在相同Talker下，性能与Qwen3Omni-30B-A3B-Thinking相当，表明E-CoT和真实世界数据可以有效补偿参数规模，在较小模型下实现高效多模态情感对话。

## 一句话评价
EmoOmni通过显式情感推理和指令指导表达，在较小模型规模下实现了高效的多模态情感对话，弥补了现有Omni-LLMs的情感智能不足。

---

