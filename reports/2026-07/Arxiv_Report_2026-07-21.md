# Arxiv Daily Deep Report - 2026-07-21

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 14
---

## 1. The tttAI System for the TSA-ASR Task of the SmartGlasses Challenge 2026

**作者**: Xuanji He, Gaoyang Dong, Xiaoxiao Li, Minchuan Chen, Fengjie Zhu
**链接**: [2607.17867](https://arxiv.org/abs/2607.17867)
**分类**: Speaker-Attributed Speech Recognition | **关键词**: TSA-ASR, speaker diarization, target-speaker extraction, overlapping speech, smart glasses, cascaded architecture

# Summary

## Core Challenges
- **Overlapping speech**: Frequent in both two-person dialogues (Track 1) and multi-party meetings (Track 2).
- **Long-form audio**: Recordings up to ~19 minutes per session.
- **Multiple speakers**: Up to 8 in Track 2, with average 4.3.
- **Smart-glasses recordings**: Challenging acoustic conditions.

## Proposed Method
Cascaded architecture comprising:
1. **Speaker Diarization**: Local EEND-style with WavLM-Large + Conformer encoder, trained on multiple datasets.
2. **Overlap Detection**: Based on diarization output, identifies regions with multiple active speakers (max 2).
3. **Target-Speaker Extraction (TSE)**: WeSep-based model with band-split RNN separator and ECAPA-TDNN speaker embeddings. Enrollment segments taken from nearest non-overlapped regions (≥5s, ≤20s).
4. **Post-Processing**: Dominant-speaker fallback: if cosine similarity between extracted signals >0.55, assign mixture to most similar speaker; other speaker drops that region.
5. **ASR Backend**: FireRedASR2-AED (1.18B parameters) using first microphone channel.

Total parameters: ~1.53B.

## Key Results
- **Track 1** (two-person dialogues): tcpCER 7.10% (5th place).
- **Track 2** (multi-party meetings): tcpCER 34.04% (2nd place on leaderboard).

## Ablation Highlights
- Using open-data + SmartGlasses data for diarization reduces DER (18.62%) and tcpCER (22.88%) compared to SmartGlasses-only or open-source baselines.
- SmartGlasses-adapted TSE improves tcpCER from 24.69% to 23.64%.
- Proposed dominant-speaker fallback reduces tcpCER from 24.69% to 22.88% on Track 2 dev set.
- FireRedASR2-AED outperforms Qwen3-ASR-1.7B (tcpCER 21.73% vs. 22.88%).
- Channel 1 is the best among four microphones.

## One-Sentence Evaluation
A well-engineered cascaded system that combines robust diarization, overlap-aware extraction, and post-processing to achieve competitive results, especially ranking 2nd on the more challenging Track 2.

---

## 2. X-Translator: A Real-Time Multilingual Speaker-Aware Speech-to-Speech Translation System

**作者**: Yuxiang Zhao, Yichi Zhang, Yanjie An, Yanqiao Zhu, Zhanxun Liu, Yushen Chen, Qixi Zheng, Haina Zhu, Yunchong Xiao, Keqi Deng, Shuai Fan, Kai Yu, Xie Chen
**链接**: [2607.17544](https://arxiv.org/abs/2607.17544)
**分类**: Speech-to-Speech Translation | **关键词**: 实时语音翻译, 多说话人, 级联系统, 流式ASR, 说话人感知

## 核心痛点
- 现有S2ST系统多为黑盒商业API或端到端模型，难以调试和替换组件；
- 长对话、多说话人场景下流式ASR假设不稳定、话轮边界模糊、需要合适的说话人提示生成目标语音。

## 方法创新
- 提出X-Translator，一种模块化级联S2ST系统，含流式ASR、MT、提示条件TTS，通过会话级运行时控制器组装；
- 增量片段提交层：将不稳定ASR流转换为稳定的翻译单元；
- 在线说话人提示管理器：绑定源语音段到说话人特定语音提示；
- 基于轻量级模型可在单张RTX 3090上运行，组件可替换。

## 实验结果
- 使用OpenSTBench评估翻译质量、语音质量、延迟；
- 与商业API（Doubao, Qwen LiveTranslate, GPT Realtime Translate）比较；
- 测量长时语音稳定性、多说话人对话说话人保持、多语言翻译质量。

## 一句话评价
X-Translator是一个开放、可复现的模块化级联S2ST系统，通过增量提交和说话人提示管理实现了实时、多说话人感知的语音翻译，为部署导向的S2ST研究提供了实用平台。

---

## 3. Adaptive Momentum Enhanced Distributed Multichannel Active Noise Control for Faster Convergence under Communication Delays

**作者**: Junwei Ji, Woon-Seng Gan, Boxiang Wang, Ziyi Yang, Haowen Li
**链接**: [2607.17165](https://arxiv.org/abs/2607.17165)
**分类**: Active Noise Control | **关键词**: Adaptive momentum, Distributed multichannel active noise control, Communication delays, Mixed-gradients distributed FxLMS, Auto-shrink step size

## 核心痛点
分布式多通道主动噪声控制（DMCANC）系统中，通信延迟会导致不稳定。现有ASSS-MGDFxLMS算法通过自动缩小步长来保证稳定性，但收敛速度显著减慢。

## 方法创新
提出自适应动量增强ASSS-MGDFxLMS（AMAS-MGDFxLMS）算法。通过余弦相似度评估瞬时梯度与动量项的方向一致性，动态调整动量因子β_k(n)=min(β_0|ρ_k(n)|^p, β_0)，当方向一致时增大动量以加速收敛，方向不一致时减小动量以保持稳定。额外计算开销仅约4L_w+2次乘法和6L_w-3次加法。

## 实验结果
在通信延迟突变场景（10s、20s、30s变化）下，MGDFxLMS发散，ASSS-MGDFxLMS稳定但收敛慢，固定动量FMAS-MGDFxLMS可能不稳定，而AMAS-MGDFxLMS实现快速收敛并保持稳定，ANSE指标更优。

## 一句话评价
一种通过自适应动量机制有效加速通信延迟下DMCANC收敛的算法，兼具稳定性和快速性。

---

## 4. SALMONN-2: Advancing General-Purpose Hearing Abilities with Self-Supervised Representations

**作者**: Xiaoyu Yang, Xuenan Xu, Wenyi Yu, Siyin Wang, Changli Tang, Terumi Chiba, Siyuan Hou, Ziyang Zhang, Wen Wu, Baoxiang Li, Guangzhi Sun, Chao Zhang, Philip Woodland
**链接**: [2607.17079](https://arxiv.org/abs/2607.17079)
**分类**: Audio Large Language Models | **关键词**: Self-supervised learning, Audio large language model, Multi-layer feature fusion, Multimodal in-context learning, SPEAR encoder

## 核心痛点
现有音频大语言模型（ALLM）大多依赖监督学习的音频编码器，受限于标注数据的质量和多样性，难以捕获超出预训练任务的声学信息。同时，多数模型使用简单适配器仅利用编码器最后一层表示，忽视了层次化表示；且缺乏对多模态上下文学习（MICL）的探索。

## 方法创新
提出SALMONN-2，基于统一的自监督学习（SSL）音频编码器SPEAR、多层特征融合（MLF）适配器和显式的MICL训练。MLF适配器聚合所有编码器层的特征，更好地利用层次化表示；通过上下文偏置训练赋予ALLM多模态上下文学习能力。

## 实验结果
在MMAU-Pro、MMAR、MMSU等基准测试中，SALMONN-2在相似规模开源模型中达到最优性能。仅用不到20K小时指令微调数据，性能超越多编码器设计。MICL能力需通过目标训练获得，而非自然涌现。

## 一句话评价
SALMONN-2验证了通用SSL音频表示作为ALLM有效基础的潜力，并通过层次特征融合与上下文学习显著提升性能。

---

## 5. An Audio Language Model-Based Voice Concept Bottleneck Framework for Interpretable Health Assessment

**作者**: Yu-Wen Chen, Julia Hirschberg
**链接**: [2607.16967](https://arxiv.org/abs/2607.16967)
**分类**: Voice-based Health Assessment | **关键词**: voice concept bottleneck, audio language model, interpretability, health assessment, depression, dysarthria

## 核心痛点
语音健康评估模型缺乏可解释性，传统方法（如openSMILE）虽提取可解释的低级声学特征，但常与不可解释特征（如MFCCs）混合使用，且概念瓶颈模型存在任务特定捷径学习、缺乏灵活适应不同健康条件的问题。

## 方法创新
提出基于音频语言模型（ALM）的语音概念瓶颈框架：
1. **解耦概念提取与下游分类**：ALM作为独立概念提取器，通过微调临床语音质量数据（PVQD）学习临床语音质量（CVQ）概念，生成离散1-5序数评分，降低任务特定捷径风险。
2. **灵活概念适应**：推理时可引入与微调不同的言语行为（SB）概念，灵活适应抑郁（行为变化）和构音障碍（运动控制障碍）等不同健康条件。
3. **增强可解释性**：离散序数评分直观易懂，配合轻量级分类器（XGBoost）可直接应用SHAP等事后可解释性方法。

## 实验结果
- 在抑郁和构音障碍评估任务上，Flamingo CVQ→SB（ALM微调CVQ后推理SB）取得最优性能，超越openSMILE和Vox-Profile等SSL基线。
- 仅用14个离散特征（5级序数）即优于依赖不可解释特征及复杂架构的基线。
- ALM离散输出比SSL连续输出更易理解且性能更佳。

## 一句话评价
本文首次将音频语言模型用于概念瓶颈框架，实现灵活、可解释的语音健康评估，在抑郁与构音障碍任务上显著优于现有方法。

---

## 6. RealDESED: A Real-World Domestic Sound Event Detection Benchmark

**作者**: Florian Schmid, Paul Primus, Alexander Fichtinger, Tara Jadidi, Tobias Morocutti, Gerhard Widmer
**链接**: [2607.16736](https://arxiv.org/abs/2607.16736)
**分类**: Sound Event Detection | **关键词**: RealDESED, Sound Event Detection, Domestic Environment, Real-World Dataset, Multi-Annotator Labeling, Temporal Event Localization

## 核心痛点
现有声音事件检测（SED）基准如DESED、UrbanSED等依赖合成声音场景或网络爬取音频，缺乏真实家庭环境的多样性（如设备、放置位置、背景噪声），且标注成本高、主观性强。

## 方法创新
本文提出RealDESED基准，包含652名参与者在家中录制的5710段真实音频（15-35秒），涵盖15类常见家庭声音。特点：
- **真实录音**：非合成或网络爬取，反映真实设备、环境、事件共现。
- **多标注者标注**：每段音频由多人独立标注，验证/测试集经审核保证质量。
- **丰富元数据**：包括录制设备、放置方式、环境标签、场景描述。
- **强基线**：基于ATST-F（预训练于AudioSet Strong）微调，测试集上PSDS1达0.731。

## 实验结果
基线性能：macro-averaged PSDS1 = 0.731 on test set。探索了标注聚合、后处理、长序列推理及元数据影响。

## 一句话评价
RealDESED填补了真实家庭环境SED基准的空白，推动从研究到部署的桥梁。

---

## 7. NABEATs: Noise-Aware Audio Representation Learning

**作者**: Takuya Fujimura, Yoshiki Masuyama, Gordon Wichern, Christoph Boeddeker, Julius Richter, Jonathan Le Roux
**链接**: [2607.16688](https://arxiv.org/abs/2607.16688)
**分类**: Audio Self-Supervised Learning | **关键词**: self-supervised learning, audio representation, noise robustness, BEATs, NABEATs, conditional denoising

# 核心痛点
现有的音频自监督学习（SSL）模型（如BEATs）在噪声环境下无法有效聚焦目标声音，导致下游任务性能显著下降。虽然语音领域已有噪声鲁棒SSL模型（如WavLM），但通用音频SSL尚未探索该方向。此外，由于音频下游任务多样，无法像说话人感知那样提供目标声音参考，而噪声参考更易获取。

# 方法创新
提出了噪声感知音频SSL概念，并基于BEATs实现了NABEATs模型。NABEATs通过额外输入参考噪声信号，学习从带噪音频中估计干净的BEATs表示。设计了两种噪声感知（NA）层：基于交叉注意力（CA）和基于FiLM，分别称为NABEATs-CA和NABEATs-FiLM。同时引入DBEATs作为无参考的去噪基线。训练时冻结原始BEATs参数，仅训练插入的附加层，使用MSE损失进行知识蒸馏。

# 实验结果
在FSD50K、US8K、SPCV2、CREMA-D、NSynth和Surge等六个下游任务上评估，模拟噪声条件（WHAM!、CHiME-3、MUSDB18）。NABEATs-CA显著优于原始BEATs和DBEATs，尤其在未见噪声类型上泛化能力更强。例如，在FSD50K上，NABEATs-CA在WHAM!噪声下mAP达45.80（原始BEATs仅35.28），且使用真实噪声时进一步提升至46.07。DCASE 2025 Task 2异常声音检测上也验证了有效性。

# 一句话评价
NABEATs通过噪声条件去噪机制有效提升了通用音频表示的噪声鲁棒性，在多种下游任务和噪声类型上均取得显著改进。

---

## 8. Pseudo-label distillation for discriminative anomalous sound detection

**作者**: Takuya Fujimura, Tomoki Toda
**链接**: [2607.16678](https://arxiv.org/abs/2607.16678)
**分类**: Anomalous Sound Detection | **关键词**: pseudo-label distillation, anomalous sound detection, self-supervised learning, noise-robust feature transformation, discriminative learning, DCASE

## 核心痛点
- 判别式异常声音检测（ASD）方法依赖详细标签（如机器参数），成本高昂。
- 自监督学习（SSL）模型虽无需标签，但计算开销大（约90M参数），不利于实际部署。

## 方法创新
- **伪标签蒸馏框架**：使用SSL模型提取特征，经K-means聚类生成伪标签，训练紧凑的判别式前端（MobileNetV2等，参数<10%）。
- **噪声鲁棒特征变换（NRFT）**：针对训练数据含噪声导致伪标签退化的问题，引入PCA子空间投影（需少量干净机器声或孤立噪声样本），抑制噪声分量。
- **联合利用粗标签与数据增强**：在蒸馏过程中，使用机器类型标签进行分簇，并采用mixup增强，进一步提升性能。

## 实验结果
- 在DCASE 2020–2025 Task 2数据集上，使用BEATs、EAT、Dasheng等四个SSL模型进行评估。
- 紧凑模型将参数和计算量（MACs）降至原SSL模型的10%以下，性能相当甚至更优。
- 伪标签蒸馏在从头训练和微调场景下均有效；NRFT方法进一步带来增益。

## 一句话评价
本文提出的伪标签蒸馏框架成功地将高昂的SSL模型性能转移到轻量级模型上，同时通过粗标签和数据增强实现超越，兼顾了效果与效率。

---

## 9. AMECxSV: Adaptive Metadata-Driven Embedding-Fusion Calibration for X-Lingual Speaker Verification

**作者**: Xin Wei, Shi He, Yihe Yuan, Huang-Cheng Chou, Sudarsana Reddy Kadiri, Shrikanth Narayanan
**链接**: [2607.16532](https://arxiv.org/abs/2607.16532)
**分类**: Automatic Speaker Verification | **关键词**: automatic speaker verification, embedding-fusion calibration, metadata-driven calibration, speaker recognition, X-lingual speaker verification

## 核心痛点
跨语言自动说话人验证（X-lingual ASV）中，固定前端系统的分数可靠性会随语言匹配度、语音时长和分数来源而变化，传统全局校准无法适应不同条件下的可靠性差异。

## 方法创新
提出AMECxSV框架，这是一个元数据驱动的嵌入融合校准后端，在元数据可用设定下工作。它融合多个固定前端系统的分数与元数据（语言匹配、时长可靠性特征），通过确定性特征扩展和MLP后端输出校准后的目标后验概率，并可选地基于后验置信度进行拒绝（AMEC-ABS）。元数据仅作为校准上下文，不直接作为说话人证据。

## 实验结果
在TidyVoiceX-ASV开发协议衍生出的说话人互斥测试集上：
- AMEC-FC（全覆盖率）将官方TidyVoice分数源的EER从3.15%降至2.42%，LI-MSV从0.64%降至0.43%。
- 双分数头（dual-score head）达到0.43%全覆盖率EER。
- 在0.79覆盖率下，AMEC-ABS达到0.03%接受试次EER。
- 通过分数仅、元数据置换、元数据仅等对照实验，验证了校准上下文解释的有效性。

## 一句话评价
AMECxSV通过元数据驱动的嵌入融合校准显著提升了跨语言说话人验证的可靠性，为多条件场景下的校准提供了轻量且有效的解决方案。

---

## 10. Dense-Sparse Dynamic Time Warping for Customizing Piano Concerto Accompaniments

**作者**: TJ Tsai, Kavi Dey, Yigitcan Ozer, Meinard Muller
**链接**: [2607.18189](https://arxiv.org/abs/2607.18189)
**分类**: Audio Alignment / Music Information Retrieval | **关键词**: Dynamic Time Warping, Dense-Sparse DTW, spectral mismatch, piano concerto accompaniment, Music Minus One

## 核心痛点
钢琴协奏曲伴奏定制中，缺乏数字化符号乐谱，且不同音频（独奏、管弦乐、混合）之间存在频谱不匹配，导致传统对齐方法效果不佳。

## 方法创新
提出 Dense-Sparse DTW（DS-DTW）算法，通过选择含有显著时间线索的音频帧（稀疏化序列）与密集序列对齐，忽略静音等不稳定区域，提高对齐鲁棒性。利用混合录音作为中介，实现无乐谱的伴奏自适应生成。

## 实验结果
在自建的四首协奏曲乐章基准上，DS-DTW 相比标准 DTW、源分离和谱减法，在相同容差下错误率更低或相当，尤其在高时间尺度修改因子下优势明显。

## 一句话评价
DS-DTW 以简洁有效的稀疏化策略解决了频谱不匹配问题，为无乐谱伴奏生成提供了实用方案。

---

## 11. FlowSonic: Stable Zero-Shot Music Editing via High-Order Trajectory Integration

**作者**: Ali Boudaghi, Hadi Zare
**链接**: [2607.17526](https://arxiv.org/abs/2607.17526)
**分类**: Music Editing | **关键词**: Music Editing, Rectified Flow, Diffusion Transformers, Numerical ODE Solvers, Zero-Shot Learning, Cross-Attention, Adams-Bashforth

## 核心痛点
- 现有零样本音乐编辑方法多针对模型生成音频而非真实录音，且依赖精心设计的提示词，编辑效果不稳定。
- 基于反演的编辑过程中，数值积分误差会累积，导致结构保留和编辑质量下降。

## 方法创新
- **FlowSonic框架**：基于预训练的整流流扩散Transformer，通过确定性反演将真实录音映射到潜空间，并在生成阶段重用反演中提取的交叉注意力表征以保留音乐结构。
- **高阶ODE求解器**：引入三阶Adams-Bashforth（AB3）积分器改善数值稳定性，并提出**动态历史缓存（DHC）**策略，利用反演阶段的速度估计初始化生成阶段的多步求解器，避免低阶预热启动带来的不一致性。

## 实验结果
- 在音色迁移和风格修改任务上，FlowSonic在语义对齐、和声保留、结构一致性和感知音频质量方面均优于现有方法。
- 通过潜轨迹可视化、梅尔频谱分析和客观指标，验证了高阶积分策略对轨迹稳定性和编辑可靠性的提升。

## 一句话评价
FlowSonic通过高阶数值积分与注意力缓存机制，实现了稳定、高保真的零样本真实音乐编辑，无需微调或配对数据。

---

## 12. Robust Summarization of Doctor-Patient Conversations: TalTech Systems for the Beyond Transcription Challenge

**作者**: Aivo Olev, Tanel Alumäe
**链接**: [2607.17230](https://arxiv.org/abs/2607.17230)
**分类**: Speech Summarization | **关键词**: speech summarization, clinical note generation, speech LLMs, reinforcement learning, medical dialogue, Voxtral, BeTraC, SOAP notes, LoRA, DAPO

## 核心痛点
临床笔记生成需要从医患对话中准确提取信息，避免幻觉，同时减少医生文书负担。传统方法依赖中间转录，而直接音频到SOAP笔记的系统需保持高可靠性。

## 方法创新
- **模型选择**：零样本测试多个开源语音LLM（Voxtral、Qwen2.5-Omni等），Voxtral因长音频鲁棒性（内部30秒分块）和低词错误率（WER）胜出。
- **两阶段微调**：
  - 监督微调（SFT）：使用LoRA（秩16）仅微调语言模型部分，冻结音频编码器和投影器。轻量级模型用音频输入，重量级模型用文本转录输入。
  - 强化学习（RL）：采用DAPO（GRPO变体）以Open Medical Concept F1为奖励，直接优化概念匹配，避免枚举概念导致的幻觉。
- **对比学习**：轻量级模型尝试生成事实表作为中间推理步骤，再生成SOAP笔记，但RL阶段仅对SOAP部分计算奖励。

## 实验结果
- **官方测试集**：轻量级赛道Concept F1=0.543，重量级赛道0.563，均获得第一。RL带来+0.04-0.05提升，且规模差异不明显（轻量级仅次重量级第二）。
- **鲁棒性**：合成到真实场景的迁移损失小（重量级仅降0.008），转录微调模型对领域偏移更鲁棒。
- **LLM评估**：重量级系统幻觉率最低（0.08%），忠实度最高（4.80），验证RL未损害事实性。Concept F1与忠实度相关性高（ρ=0.91）。

## 一句话评价
该系统通过零样本筛选语音LLM、两阶段微调（SFT+DAPO RL）直接优化临床概念F1，在BeTraC挑战中赢得双赛道第一，并保持低幻觉率，证明任务指标优化与事实可靠性可兼得。

---

## 13. Is One Score Enough? Assessing Singing Quality of Songs with Temporal Score Curves

**作者**: Yishan Lv, Jing Luo, Xinyu Yang, Zhizheng Wu
**链接**: [2607.16599](https://arxiv.org/abs/2607.16599)
**分类**: Singing Quality Assessment | **关键词**: Singing Quality Assessment, Full-length Song, Temporal Score Curve, Self-Supervised Learning, Transformer

## 核心痛点
- 现有歌唱质量评估（SQA）主要针对短片段（clip-level），无法捕捉完整歌曲中不同段落（如主歌、副歌、桥段）的质量变化。
- 段级标注稀缺，简单地将整体分数分配给每个段落会导致标签共享假设，忽略细粒度差异。

## 方法创新
- 提出SongSQA框架，包含两个阶段：
  - **Segment Score Predictor**：利用教师模型生成的伪标签训练，实现段级质量预测，无需人工段级标注。
  - **Song Quality Aggregator**：通过可学习的歌曲嵌入和Transformer自注意力机制，动态聚合关键时刻（如表达性副歌或明显缺陷）的信息，预测整体分数并生成时间质量曲线。

## 实验结果
- 在所有数据集上，SongSQA在KTAU指标上相比最强基线提升高达13.95%，其他评估指标也一致提升。

## 一句话评价
SongSQA首次将SQA从短片段扩展到完整歌曲，同时输出整体分数和段级质量曲线，有效解决了质量变化和非均匀感知问题。

---

## 14. Comparing Spectrogram Front-Ends for Abnormal Heart-Sound Detection with a Convolutional Neural Network

**作者**: Abhinav Pala, Dhanush Pala
**链接**: [2607.16220](https://arxiv.org/abs/2607.16220)
**分类**: Heart Sound Classification | **关键词**: spectrogram, PCEN, multi-resolution, heart sound, convolutional neural network, PhysioNet 2016, abnormal detection

## 核心痛点
心音检测作为低成本心血管疾病筛查手段，其性能高度依赖音频预处理方式（前端）。此前研究多关注分类器本身，但忽略了输入表示（如频谱图计算方式）的影响。

## 方法创新
固定一个紧凑的2D CNN，仅改变三种频谱图前端：
1. 标准对数梅尔频谱（log-mel）；
2. 逐通道能量归一化（PCEN），自适应调整每个频率通道的增益；
3. 多分辨率对数梅尔频谱（multi-resolution），堆叠不同FFT窗口尺寸（256,512,1024）的三通道图像。
所有前端输出均标准化为零均值单位方差，训练策略（优化器、学习率、批次大小、epoch数）完全一致。

## 实验结果
在PhysioNet 2016心音数据集（3240条录音，79.5%正常/20.5%异常）上：
- 三种前端的敏感性均约0.95；
- PCEN与多分辨率的官方修正准确率（MAcc）分别为0.915和0.916，优于基础log-mel的0.910；
- 使用Grad-CAM发现模型主要关注低频（S1/S2心音区域）。

## 一句话评价
通过精心设计的控制实验，明确证明PCEN和多分辨率频谱图作为前端能小幅提升心音异常检测性能，且模型确实学到了生理相关特征。

---

