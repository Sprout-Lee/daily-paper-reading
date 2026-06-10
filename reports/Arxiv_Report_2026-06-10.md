# Arxiv Daily Deep Report - 2026-06-10

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 19
---

## 1. Optimizing 2D Input Representations and Sub-phase Fusion Strategies for Differential Diagnosis of Asthma and COPD Using CNN- and GRU-Based Networks

**作者**: Ipek Sen, Ozgur Ozdemir, Elena Battini Sonmez
**链接**: [2606.10972](https://arxiv.org/abs/2606.10972)
**分类**: Audio Signal Processing / Pulmonary Sound Classification | **关键词**: asthma, COPD, pulmonary sounds, deep learning, CNN, GRU, MFCC, spectrogram, VAR model, sub-phase fusion

## 核心痛点
哮喘和慢性阻塞性肺病（COPD）的鉴别诊断在临床上存在困难，因症状重叠易误诊。传统方法如肺功能测试依赖患者配合，且听诊主观性强。现有肺音分析研究多使用单一通道或全周期，未充分利用呼吸子阶段的时间信息，且二维表示（如声谱图）存在时域维度不一致问题。

## 方法创新
1. **二维输入表示优化**：比较VAR矩阵、MFCC和log-mel谱图三种表示，提出自适应长度加窗以统一各子阶段（早、中、晚吸气和呼气）的时域维度，并通过网格搜索优化频谱和时间分辨率。
2. **子阶段融合策略**：使用CNN提取各子阶段的二维特征，然后采用直接拼接、GRU网络、GRU+注意力机制三种方式融合子阶段特征，以利用呼吸周期内的时序信息。
3. **数据增强**：测试了多种数据增强技术（包括mixup）以缓解小数据集问题。

## 实验结果
- 基于呼吸周期的最佳F1分数：0.877（MFCC，13系数，64点时间分辨率，直接特征拼接）
- 基于受试者的最佳F1分数：0.855（MFCC，13系数，256点时间分辨率，全周期表示，自适应长度加窗）
- MFCC优于log-mel谱图和VAR模型；复杂的融合策略（GRU/注意力）未提升性能；数据增强整体降低性能，但mixup相对最佳。

## 一句话评价
本文系统优化了肺音二维输入表示和子阶段融合策略，证明MFCC配合简单直接拼接在哮喘与COPD鉴别中效果最佳，且数据增强并非总是有益。

---

## 2. Phoneme-First Prediction for LLM-Based Speech Recognition

**作者**: Jakob Poncelet, Hugo Van hamme
**链接**: [2606.10864](https://arxiv.org/abs/2606.10864)
**分类**: Speech Recognition | **关键词**: phoneme-first, speech recognition, large language model, ASR, speech LLM

## 论文总结：Phoneme-First Prediction for LLM-Based Speech Recognition

### 核心痛点
语音增强型大语言模型（speech-augmented LLM）面临语音特征与文本语义对齐的挑战。传统方法直接映射语音到文本，忽略了发音细节，导致同音词混淆，且在低资源场景下性能受限。

### 方法创新
提出**音素优先（Phoneme-First）** 方法，修改LLM提示词为“先转录为音素，再转录为文本”，让模型先预测音素序列，再生成最终转录。音素标签可从现有文本自动生成，无需额外标注。同时提出联合训练（Joint）策略，随机混合标准S2T和音素优先指令，提升泛化能力。

### 实验结果
- 在LibriSpeech-100h和TEDLIUM-100h上，联合训练的PF-S2T相比标准S2T显著降低WER，尤其在TEDLIUM上达到25%的改进。
- 在LibriSpeech-960h全量数据上，联合训练仍带来提升，且对自监督编码器（HuBERT）同样有效。
- 音素优先方法在低资源场景下优势更明显，且输出转录在声学上更忠实于原始语音。

### 一句话评价
一种简单、低成本且有效的音素中间预测策略，能显著提升LLM语音识别的准确性和可解释性。

---

## 3. Speech Encoder Fusion for LLM-based Automatic Speech Recognition

**作者**: Jakob Poncelet, Hugo Van hamme
**链接**: [2606.10853](https://arxiv.org/abs/2606.10853)
**分类**: Speech Recognition | **关键词**: speech LLM, encoder fusion, automatic speech recognition, multilingual ASR, Whisper, NeLF, Wav2vec2

## 核心痛点
现有语音感知LLM通常仅使用单个预训练语音编码器，其性能受限于编码器的特定优势，不同编码器往往具有互补性但未被有效利用。

## 方法创新
提出多种语音编码器融合策略，包括：特征拼接、Sigmoid门控、多头注意力门控、位置Transformer和时间Transformer。这些方法在保持序列长度不变的情况下，通过可学习的权重或注意力机制动态组合多个编码器的输出，以利用其互补优势。

## 实验结果
- 荷兰语ASR：融合Whisper和NeLF编码器，时间Transformer取得最佳WER（clean 6.8%, other 8.3%），优于单个编码器（Whisper: 8.3%/11.5%, NeLF: 7.5%/9.0%）。
- 英语ASR：融合Whisper和Wav2vec2，时间Transformer再次最优（clean 2.6%, other 5.5%），优于Whisper（3.2%/6.4%）和Wav2vec2（2.9%/6.8%）。
- 多语言场景：融合策略在保持多语言能力的同时提升目标语言性能。
- 计算开销：并行编码器增加有限，融合层参数仅约30M。

## 一句话评价
本文系统性地探索了多种语音编码器融合策略，实验证明基于时间Transformer的融合方法在单语和多语ASR中均能显著提升性能且计算开销可控。

---

## 4. Towards Deep Contextual Reasoning from Broad Descriptions for ASR with Speech-LLM via Metadata-Driven Reasoning Chains

**作者**: Jakob Poncelet, Hugo Van hamme
**链接**: [2606.10838](https://arxiv.org/abs/2606.10838)
**分类**: Speech Recognition | **关键词**: speech LLM, contextual biasing, chain-of-thought reasoning, metadata-driven, contextual ASR

## 核心痛点
当前ASR在罕见领域术语和上下文相关的命名实体上识别效果差，现有上下文偏置方法主要依赖关键词列表，无法进行深层推理。

## 方法创新
提出一种元数据驱动的推理链训练方法，利用视频描述等广域文本作为弱语义先验，构建400小时推理增强数据（包含ASR错误和LLM生成错误）。通过两阶段流程：先由文本LLM生成推理链（解释基于上下文的修正理由），再微调Speech-LLM执行链式推理（初始转录→上下文推理→最终转录），使模型在保持音频依据的同时实现深度上下文修正。

## 实验结果
在YouTube衍生的M³AV测试集上，该方法降低了整体词错误率，尤其在罕见词和命名实体上表现显著提升，为语音识别中的深度上下文推理奠定了基础。

## 一句话评价
开创性地将链式推理引入语音识别上下文推理，实现从广域描述到深度上下文校正，兼具音频依据与主题一致性。

---

## 5. Recovering the Zipfian Distribution in Unsupervised Term Discovery

**作者**: Danel Slabbert, Simon Malan, Herman Kamper
**链接**: [2606.10781](https://arxiv.org/abs/2606.10781)
**分类**: Zero-resource Speech Processing，Unsupervised Term Discovery | **关键词**: word segmentation, unsupervised term discovery, Zipfian distribution, graph clustering, Leiden algorithm

## 核心痛点
无监督术语发现中，主流中心聚类方法（如K-means）因归纳偏置产生近似均匀的类别频率分布，无法反映自然语言的长尾Zipfian分布。

## 方法创新
1. 采用**图聚类**（Leiden算法+Constant Potts Model）作为自底向上替代方案，通过相似度阈值τ和分辨率参数γ控制聚类粒度。
2. 对比三种中心方法（K-means、BIRCH、FBGMM）和两种自底向上方法（图聚类、层次平均链接聚类）。
3. 在三种分割粒度（真实词边界、真实音节边界、无监督音节分割）和三种语言（英语、南非荷兰语、法语）上系统评估。

## 实验结果
- 图聚类在词级和音节级词汇发现上全面优于中心方法，产生更接近Zipfian的分布。
- 层次平均链接聚类也表现良好，但计算效率较低且分布控制能力弱。
- 中心方法（尤其K-means）产生均匀分布，与自然语言分布严重不符。

## 一句话评价
本文质疑了中心聚类在术语发现中的主导地位，提出图聚类作为有效且可解释的替代方案，能更好地恢复词汇的Zipfian分布。

---

## 6. Anchoring the Unknown: Open-Set Model Attribution via Proxy-Anchor Learning

**作者**: Cristian-Teodor Neamtu, Serban Mihalache, Stefan Smeu, Dan Oneata, Horia Cucu, Dragos Burileanu
**链接**: [2606.10758](https://arxiv.org/abs/2606.10758)
**分类**: Audio Forensics, Text-to-Speech | **关键词**: Open-Set Model Attribution, Proxy-Anchor Loss, OOD Detection, Deep Metric Learning, Audio Forensics, Text-to-Speech, MLAAD Dataset

## 核心痛点
- TTS系统合成语音的溯源（source tracing）在开放集场景下研究不足，未知系统可能被遇到。
- 现有方法大多假设固定已知系统集，且将同架构不同版本视为独立类别，导致类间混淆。

## 方法创新
- 提出基于Proxy-Anchor损失函数的度量学习框架，使用Wav2Vec2-BERT提取帧级特征并聚合为1024维话语级嵌入。
- 引入架构合并策略（architecture merging），将同架构不同版本的TTS系统归为一类，减少类间混淆。
- 后处理OOD检测：使用softmax能量、香农熵或最大代理距离作为得分，基于阈值判断OOD。

## 实验结果
- 在MLAAD v9数据集上，110个ID类达到99.76%准确率，OOD检测FPR@95低至2.04%。
- 与SOTA相比，OOD准确率几乎翻倍。
- 对比基线：Logistic Regression和k-NN，Proxy-Anchor在ID分类上接近，OOD上显著优于。

## 一句话评价
该工作将Proxy-Anchor度量学习与架构合并策略结合，有效解决了开放集TTS溯源问题，性能达到SOTA。

---

## 7. Spatial-Omni: Spatial Audio Understanding Integration in Multimodal LLMs via FOA Encoding

**作者**: Zhiyuan Zhu, Yixuan Chen, Yiwen Shao, Wenxiang Guo, Changhao Pan, Yu Zhang, Yuxiang Wang, Wei Liu, Houhua Zhang, Chengkuan Zeng, Wenbo Cheng, Yunxi Liu, Rui Yang, Steve Yves, Liefeng Bo, Zhou Zhao
**链接**: [2606.10738](https://arxiv.org/abs/2606.10738)
**分类**: Spatial Audio Understanding in Multimodal LLMs | **关键词**: Spatial-Omni, First-Order Ambisonics (FOA), spatial audio understanding, multimodal large language model, SO-Encoder, spatial token, SO-Dataset, SO-Bench

**核心痛点**：当前多模态大模型主要处理单声道音频，丢弃了空间音频中的方向、距离、运动等空间线索，导致无法进行声音定位、空间关系推理和空间场景理解。现有空间音频LLM方法需大幅修改或重新训练原始音频编码器，可能损害语义能力且缺乏灵活性。同时，大规模FOA空间音频QA数据和系统化基准缺失。

**方法创新**：提出**Spatial-Omni**，通过轻量级**SO-Encoder**将一阶Ambisonics（FOA）空间音频作为独立模态注入现有Omni LLM，无需修改原始音频编码器。SO-Encoder并行于原始音频编码器，接收4通道FOA梅尔特征和3通道强度向量（IV）特征，提取时空线索，并通过Temporal Pixel Shuffle Projector压缩为紧凑空间token，与音频、视觉、文本token联合推理。训练采用两阶段：先基于SELD指标监督训练SO-Encoder，再使用空间QA对微调整个模型。

**实验结果**：在构建的**SO-Bench**（16个子任务，涵盖基础检测、空间关系、复杂推理）上，Spatial-Omni显著优于现有开源大音频语言模型和Omni LLM，同时保持通用音频理解能力。消融实验证实性能提升主要来自真实空间token。

**数据集**：构建**SO-Dataset**（约40万FOA空间音频片段）和**SO-QA**（210万空间问答对），数据来源包括公开SELD数据集、真实录音和仿真。

**一句话评价**：首个以独立模态方式集成FOA空间音频到Omni LLM的轻量化框架，有效提升空间音频理解性能且不影响原有语义能力。

---

## 8. GC-LoRA: Gated Convolutional LoRA for Parameter-Efficient Acoustic Adaptation

**作者**: Natarajan Balaji Shankar, Zilai Wang, Kaiyuan Zhang, Mohan Shi, Abeer Alwan
**链接**: [2606.10464](https://arxiv.org/abs/2606.10464)
**分类**: Automatic Speech Recognition | **关键词**: Automatic Speech Recognition, Domain Adaptation, Parameter Efficient Fine-Tuning, Low-Rank Adaptation (LoRA), Conformer, Gated Convolution, Child Speech, Dialectal Speech

## 核心痛点
Transformer-based Speech Foundation Models 在处理声学特性不匹配的目标域（如环境退化、带限、方言、儿童语音）时性能显著下降，而全量微调成本高。现有 PEFT 方法（如 LoRA）仅调整全局注意力，缺乏局部上下文建模，无法有效捕获域特定的声学变化。

## 方法创新
提出 **GC-LoRA (Gated Convolutional LoRA)**，在 LoRA 瓶颈中嵌入 Conformer 风格的门控深度可分离卷积，专门应用于注意力输出投影 (W_o)，以在不破坏预训练全局表示的前提下高效捕获局部声学依赖。通过低秩空间内的点卷积、门控线性单元 (GLU)、深度卷积、组归一化和 Swish 激活实现局部特征细化，保持与 LoRA 相近的参数效率。

## 实验结果
在 AMI（混响/噪声）、Switchboard（电话带宽限制）、CORAAL（非裔美国英语方言）、MyST（儿童语音）四个挑战性数据集上，以 Whisper-Medium 为骨干，GC-LoRA 相较标准 LoRA 取得 **Word Error Rate (WER) 最高降低 10.9%**，且参数量增长极小。全面优于 Zero-Shot、Full Finetuning、Adapter、LoRA-Output、Conv-LoRA、MultiConv-LoRA 等基线。

## 一句话评价
GC-LoRA 通过轻量级门控卷积注入局部声学归纳偏置，在多种声学域自适应任务中以极小额外参数达成显著性能提升，是一种结构更优的 PEFT 方法。


---

## 9. Entropy-Aware Domain-Routed Mixture-of-Experts Speech-LLM Framework: A Case Study of Multi-Domain Child-Adult ASR

**作者**: Mohan Shi, Kaiyuan Zhang, Zilai Wang, Natarajan Balaji Shankar, Eray Eren, Abeer Alwan
**链接**: [2606.10454](https://arxiv.org/abs/2606.10454)
**分类**: Error | **关键词**: 

总结生成失败: Expecting value: line 1 column 1 (char 0)

---

## 10. SSL-GMMVC: Interpretable Voice Conversion via Locally Linear GMM Transforms in Self-Supervised Representation Space

**作者**: Tomoya Tanabu, Hiroshi Nishijima, Daisuke Saito, Nobuaki Minematsu
**链接**: [2606.10317](https://arxiv.org/abs/2606.10317)
**分类**: Voice Conversion | **关键词**: voice conversion, self-supervised learning, Gaussian mixture model, interpretable, locally linear transform

## 核心痛点
现有语音转换方法要么依赖复杂深度神经网络缺乏可解释性（如FreeVC），要么使用全局线性变换（如LinearVC）无法适应局部结构，导致表达力有限。

## 方法创新
提出SSL-GMMVC，在自监督学习（SSL）特征空间中使用高斯混合模型（GMM）对源-目标特征联合分布建模，转换时通过后验加权求和实现局部线性仿射变换，兼具可解释性与表达力。提供了全协方差和跨对角协方差两种变体。

## 实验结果
- 客观指标：SSL-GMMVC在说话人相似度（EER）上随训练数据增加稳步提升，在N≥100时超过LinearVC，且多数配置优于FreeVC；可懂度（WER）和自然度（UTMOS）与基线相当或更优。
- 主观指标：相似度MOS在N≥20时超过FreeVC，自然度在N≥20后接近FreeVC。
- 进一步分析：混合分量选择与音系类别（响音/阻塞音）相关，变换矩阵具有可解释的缩放和旋转特性。

## 一句话评价
一种在自监督表示空间中使用局部线性GMM变换的可解释语音转换方法，兼顾性能与可分析性。

---

## 11. ANCHOR: Autoregressive Non-intrusive Chunk-Ordered Refinement for Joint Multi-Resolution Speech Quality Modeling

**作者**: Zhuoyan Tao, Jiatong Shi, Hye-jin Shim, Shinji Watanabe
**链接**: [2606.10233](https://arxiv.org/abs/2606.10233)
**分类**: Speech Quality Assessment | **关键词**: incremental evaluation, autoregressive modeling, pseudo-MOS, multi-resolution, speech quality assessment

# ANCHOR: Autoregressive Non-intrusive Chunk-Ordered Refinement for Joint Multi-Resolution Speech Quality Modeling

## 核心痛点
- 传统语音质量评估方法（如PESQ、ViSQOL）以及非侵入式方法（如UTMOS、DNSMOS）均假设完整话语可用，无法在部分输入（前缀）场景下进行增量评估。
- 局部失真（如丢包、裁剪）在全局池化中会被弱化，导致早期质量估计不准确。
- 自监督学习（SSL）模型深层表征对局部信号不敏感，加剧了局部-全局耦合问题。

## 方法创新
- **多分辨率自回归建模**：在ARECHO基础上，引入双分辨率（块级和话语级）度量查询令牌，统一解码框架内联合预测。
- **分辨率感知解码顺序**：强制先预测块级度量，再预测话语级度量，实现从粗到细的层次化细化，避免多任务冲突。
- **离散自回归目标**：将连续值分位箱化为500个令牌，通过交叉熵优化，并采用教师强制训练。

## 实验结果
- 在2秒前缀下，PLCMOS误差降低48%（与ARECHO相比）。
- 收敛分析显示有效感知上下文窗口为4-6秒。
- 压力测试表明模型在局部损坏下保持稳定外推，避免过拟合截断边界。
- 在2s、4s、6s、8s前缀长度上，ANCHOR的块级MAE均优于ARECHO，尤其在PLCMOS上优势显著。

## 一句话评价
ANCHOR通过层次化多分辨率自回归框架，首次实现了对伪MOS度量的增量预测，在部分输入场景下显著优于现有全上下文模型。

---

## 12. LLM can Read Spectrogram: Encoder-free Speech-Language Modeling

**作者**: Ruchao Fan, Yiming Wang, Yuxuan Hu, Bo Ren, Yufei Xia, Xiaofei Wang, Yao Qian, Jinyu Li
**链接**: [2606.10231](https://arxiv.org/abs/2606.10231)
**分类**: Speech-Language Modeling | **关键词**: Encoder-free, Mel spectrogram, ASR, TTS, Large Language Model, LoRA, Phi-4-MM

## 核心痛点
传统Speech-LLM依赖专用语音编码器（如Whisper、Conformer），带来计算开销大、表示不匹配、信息瓶颈等问题。

## 方法创新
提出**Mel-LLM**，一种无编码器架构：仅保留卷积下采样层和线性投影，将Mel频谱图分块直接输入LLM（Phi-4-MM），使LLM自身学习语音-文本对齐。ASR和TTS共享同一LLM骨干，通过LoRA适配。TTS使用连续V AE解码器生成Mel频谱图。

## 实验结果
- **ASR**（OpenASR）：无编码器Mel-LLM平均WER 7.12%，仅比随机初始化编码器基线（6.97%）差0.15%，且随数据规模扩大差距缩小（从11.3%降至3.8%）。
- **TTS**：初步结果，零样本合成WER 12.4%，UTMOS 3.8，尚非最优但证明可行性。
- 消融实验表明：低层LLM层对语音理解贡献大；Phi-4-MM多模态预训练初始化在数据有限时至关重要。

## 一句话评价
首次系统证明LLM可无需专用语音编码器直接理解并生成连续Mel频谱图，为统一语音-文本建模提供了简洁高效的Encoder-free范式。

---

## 13. DeRA-MOS: Optimizing Text-to-Music Evaluation via Decoupled Listwise Ranking and Modality Alignment

**作者**: Chien-Chun Wang, Hung-Shin Lee, Hsin-Min Wang, Berlin Chen
**链接**: [2606.10010](https://arxiv.org/abs/2606.10010)
**分类**: Text-to-Music Evaluation | **关键词**: Text-to-music evaluation, mean opinion score, listwise ranking, cross-modal alignment, metric learning

### 核心痛点
- 文本到音乐（TTM）系统评估依赖人类平均意见分数（MOS），成本高且难以规模化。
- 现有自动MOS估计器采用逐点回归或分布分类，未直接优化排序指标（如SRCC），且缺乏跨模态一致性的几何约束。

### 方法创新
- 提出DeRA-MOS，一个解耦优化框架，包含两个专用损失：
  - **Batch-Aware Listwise Ranking (BALR)**：用于音乐印象（MI），将小批量视为排序列表，通过温度缩放softmax将预测和真值分布化，并计算交叉熵损失，直接优化全局排序。
  - **Score-Anchored Modality Alignment (SAMA)**：用于文本对齐（TA），在跨注意力融合前，将音频-文本余弦相似度线性映射到[0,1]并与归一化的人类TA MOS对齐（MSE损失），防止表示漂移。
- 联合优化：L_total = L_CE-Gauss + α*L_BALR + β*L_SAMA，其中α=0.2, β=0.3。
- 推理时无额外参数/FLOPs，保持基线复杂度。

### 实验结果
- 在MusicEval数据集上，DeRA-MOS相比基线DORA-MOS及再实现版本取得一致提升：
  - MI: SRCC 0.989 (vs DORA-MOS* 0.988), KTAU 0.940 (vs 0.913)
  - TA: SRCC 0.956 (vs 0.944), KTAU 0.835 (vs 0.809)
- 消融实验显示BALR和SAMA均有效，且联合效果最佳。

### 一句话评价
DeRA-MOS通过解耦的列表排序和模态对齐损失，显著提升了TTM评估的排序一致性，是高效鲁棒的大规模评估框架。

---

## 14. Multi-Faceted Interactivity Alignment in Full-Duplex Speech Models

**作者**: Atsumoto Ohashi, Neil Zeghidour, Alexandre Défossez, Eugene Kharitonov
**链接**: [2606.11167](https://arxiv.org/abs/2606.11167)
**分类**: Speech Dialogue Systems | **关键词**: Full-duplex speech, Reinforcement learning, Interactivity alignment, GRPO, Pause handling, Turn-taking, Backchanneling, User interruption

## 核心痛点
现有全双工口语对话模型仅通过监督学习（token级似然最大化）训练，无法直接优化交互级行为，导致交互性问题，如过度沉默、时机不当的轮换、缺乏背面通道等。

## 方法创新
提出基于强化学习的后训练对齐方法，全面改善全双工模型的交互性。具体包括：
1. 针对四个核心交互轴（暂停处理、轮换、背面通道、用户打断），从人类对话语料中自动提取短音频片段。
2. 使用轴特定奖励函数，通过组相对策略优化（GRPO）进行优化。
3. 额外引入基于LLM的奖励（LLM Judge）防止语义质量下降。

## 实验结果
在两个开源模型（Moshi和PersonaPlex）上应用该方法，在Full-Duplex-Bench v1（离线评估）和v2（实时多轮对话评估）上均取得一致的交互性改进。

## 一句话评价
该工作首次系统性地通过RL全面优化全双工模型的多个交互维度，并验证了跨模型泛化性。

---

## 15. Data-Driven Runway and Taxiway Exits Prediction of Landing Aircraft: A Case Study at Hartsfield-Jackson Atlanta International Airport

**作者**: Alex Porcayo, Yutian Pang, Maria Thomas, John-Paul Clarke
**链接**: [2606.11017](https://arxiv.org/abs/2606.11017)
**分类**: Air Traffic Management / Airport Operations | **关键词**: Runway Exit Prediction, Taxiway Crossing Prediction, Data-Driven, Machine Learning, Situational Awareness, ASDE-X, Imbalanced Classification, Class Overlap

## 核心痛点
机场场面运行（尤其是高吞吐量枢纽）成为系统性能的瓶颈。着陆飞机的跑道出口选择和是否穿越活跃离场跑道（或使用端绕滑行道）的决策依赖复杂、上下文相关的因素（如进近速度、机型、机位、交通率、天气），且现有预测模型多为二元分类，忽略了实际运行中多个出口的差异和少数类样本的预测问题。

## 方法创新
提出一个两阶段数据驱动的决策辅助框架，模仿管制员工作流：阶段I预测着陆飞机选择的跑道出口（每个流向三个候选出口），阶段II基于该出口预测飞机是否穿越离场跑道或使用端绕滑行道。模型使用ASDE-X轨迹数据、飞机属性、机位目的地、短期交通率（到达、离场、穿越使用）、机场天气等多个特征窗口。基准测试九种分类器（包括线性模型、神经网络、树集成），重点评估随机森林、XGBoost、LightGBM、CatBoost，并采用不平衡感知指标（macro-F1、精确率-召回率曲线、混淆矩阵、Brier分数、预期校准误差）。

## 实验结果
- 阶段I准确率0.86-0.89，macro-F1 0.40-0.50；阶段II准确率0.70-0.74，macro-F1 0.28-0.55。
- XGBoost和LightGBM表现优于随机森林。
- 特征重要性分析：进近速度主导出口选择；离场率、穿越率、机位目的地和（西流）已选出口是穿越vs端绕的最强预测因子。
- 类别重叠分析（t-SNE和UMAP）表明特征空间不可分性是少数类预测的主要瓶颈；概率校准确认输出校准良好。
- 精确率-召回率和混淆矩阵暴露了类别不平衡效应，需采用不平衡感知训练。

## 一句话评价
本文提供了一个可解释的管制员决策支持工具，通过两阶段预测增强了态势感知，但少数类预测受类别重叠限制，需进一步处理不平衡问题。

---

## 16. Multilingual Word-Level Forced Alignment with Self-Supervised Representations and Learned Dynamic Programming

**作者**: Roy Weber, Meidan Zehavi, Rotem Rousso, Joseph Keshet
**链接**: [2606.10675](https://arxiv.org/abs/2606.10675)
**分类**: Speech Recognition | **关键词**: forced alignment, word alignment, self-supervised representation, multilingual, dynamic programming

## 核心痛点
传统HMM-GMM在强制对齐任务中仍占主导，但多语言泛化能力有限；现有自监督方法（如MMS的CTC对齐）精度不足，尤其在不同语言上表现不稳定。

## 方法创新
提出双阶段架构：1）**对齐编码器**：融合MMS（CTC词置信度）和UnSupSeg（无监督音素边界检测）两种自监督表示，采用Conformer/VGG等骨干网络进行边界概率预测；2）**对齐解码器**：可学习动态规划模块，利用四个特征函数（UnSupSeg距离、编码器输出、归一化和、MMS字符似然）联合优化，支持约束词长。训练采用分步迭代：先独立训练编码器（焦点损失解决类别不平衡），再与解码器交替微调。

## 实验结果
- 在TIMIT和Buckeye上，Conformer编码器F1达43.0%/39.1%，优于VGG和Transformer。
- 完整系统在英语数据集上超越MFA和MMS基线（表略）。
- 在未见语言（荷兰语、德语、希伯来语）上，50ms以上容差时性能最优或持平，展现多语言扩展潜力。

## 一句话评价
通过自监督表示融合与可学习动态规划，实现了超越传统工具的多语言词级强制对齐，尤其为难标注语言提供了零样本方案。

---

## 17. ParaBridge: Bridging Paralinguistic Perception and Dialogue Behavior in Speech Language Models

**作者**: Yuxiang Wang, Qinke Ni, Shengbo Cai, Wan Lin, Liqiang Zhang, Zhizheng Wu
**链接**: [2606.10581](https://arxiv.org/abs/2606.10581)
**分类**: Speech Language Models / Dialogue Systems | **关键词**: Speech Language Models, Paralinguistic Perception, Perception-Behavior Gap, Self-Distillation, Scaffold, Dialogue Behavior

## 核心痛点
当前的语音语言模型（SLM）能够感知副语言线索（如说话者身份、情绪、背景噪音等），但在开放域对话中往往忽略这些线索，导致模型在需要根据副语言线索调整回复的场景下表现不佳。例如，Qwen3-Omni-thinking在VoxSafeBench儿童声音任务中的安全感知率（SAR）仅为6.1%，尽管它能在MMSU副语言相关任务中达到52.8%。这种“感知-行为差距”是论文要解决的核心问题。

## 方法创新
论文提出ParaBridge，一种在线自蒸馏（on-policy self-distillation）框架。其核心思想是：利用模型本身在推理时加入副语言指令脚手架（scaffold）后表现出的良好行为，来指导无脚手架模型的学习。具体而言，对于每个音频样本，模型被查询两次：一次无脚手架（学生）生成回复轨迹，一次有脚手架（教师）提供沿该轨迹的完整词汇分布。通过逐token的Jensen-Shannon散度损失，将教师的副语言感知行为蒸馏到学生中。该方法无需外部监督数据、人工标注或奖励模型，且训练时学生采用在线采样，避免了分布不匹配。

## 实验结果
在Qwen3-Omni-thinking上，ParaBridge将无脚手架模型的VoxSafeBench SAR从14.6%提升至40.3%（甚至有脚手架基线仅29.0%），EchoMind平均评分从3.27提升至3.92。通用能力方面，MMAU-Pro、VoiceBench和GPQA与原始模型差距均在0.4分以内。该方法还泛化到未见过的副语言线索、从安全导向训练迁移到共情导向对话，并在不同SLM主干（MiMo-Audio-thinking）上验证有效。数据效率高，仅需500个学生rollout即可达到37.6% SAR。

## 一句话评价
ParaBridge通过在线自蒸馏，无需外部监督即可有效缩小SLM的副语言感知-行为差距，显著提升对话中的副语言响应能力，同时保持通用能力。

---

## 18. A Lightweight Dual-Factor Acoustic Authentication System via Cascaded GMM-DTW Architecture for Edge Computing

**作者**: Yutong Zhang
**链接**: [2606.10565](https://arxiv.org/abs/2606.10565)
**分类**: Acoustic Authentication | **关键词**: 轻量级双因素声学认证, GMM-DTW级联架构, 边缘计算, MFCC特征重用, 动态似然空间约束

## 核心痛点
传统深度学习声纹认证在边缘设备上面临计算资源瓶颈（GPU依赖、高延迟）和单因素认证的安全漏洞（易受假体攻击和高保真重放）。

## 方法创新
提出一种轻量级双因素级联架构：
1. **共享MFCC特征提取**：20维静态MFCC + 20维一阶Delta，共40维特征，下游分类器复用；
2. **第一因素GMM说话人筛选**：对角协方差GMM，含自适应概率阈值和动态联合绝对-相对边际约束（DLSC），抵御未知说话人和重放攻击；
3. **第二因素DTW口令验证**：基于Sakoe-Chiba窗口约束的DTW，保证确定性延迟。

## 实验结果
- 物理冒充FAR: 2.73%，高保真重放FAR: 6.67%，合法FRR: 16.67%；
- 端到端延迟: 9.82 ms（单核CPU），其中特征提取1.51 ms，GMM评分0.54 ms，DTW最坏情况7.77 ms。

## 一句话评价
一种在资源受限边缘设备上实现高安全、低延迟的轻量级声学双因素认证方案。

---

## 19. Enhancing Multilingual LLM-based ASR with Mixture of Experts and Dynamic Downsampling

**作者**: Guodong Lin, Ziqi Chen, Yuxiang Fu, Ke Li, Wei-Qiang Zhang
**链接**: [2606.10439](https://arxiv.org/abs/2606.10439)
**分类**: Speech Recognition | **关键词**: multilingual ASR, large language model, Mixture of Experts, Continuous Integrate-and-Fire, modality alignment

## 核心痛点
多语言泛化能力弱、模态对齐困难，现有LLM-ASR框架在跨语言场景下性能下降明显。

## 方法创新
1. **MoE增强投影器**：引入混合专家架构，通过门控路由动态选择专家子网络，提升跨语言适应性。
2. **CIF动态下采样**：采用连续积分-触发机制，预测文本token数量并动态聚合音频特征，实现更精确的模态对齐。

## 实验结果
在1500小时多语言数据集上，提出的方法（MoE + modified CIF）相比基线LLM-ASR在MLCSLM-dev上WER从23.26%降至15.27%，在CommonVoice-test上从19.57%降至13.87%，在FLEURS-test上从13.05%降至10.46%。扩展至8000小时训练后，进一步在所有测试集上超越Whisper-large-v3。

## 一句话评价
该工作通过MoE和CIF有效提升了多语言LLM-ASR的准确性和鲁棒性。

---

