# Arxiv Daily Deep Report - 2026-05-25

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 7
---

## 1. Natural Yet Challenging to Detect: Robust In-the-Wild TTS through EMA and Dual-Scoring Prompt Selection -- Submission for WildSpoof 2026 TTS Track

**作者**: Renhe Sun, Jiayi Zhou, Haolin He, Yueying Feng, Jian Liu
**链接**: [2605.23859](https://arxiv.org/abs/2605.23859)
**分类**: Text-to-Speech | **关键词**: WildSpoof Challenge, Text-to-Speech, Exponential Moving Average, Dual-scoring Prompt Selection, F5-TTS, In-the-Wild, Spoofing Detection

## 论文总结

**核心痛点**：在嘈杂、声学多样化的现实场景中，传统TTS模型表现不佳，且高质量语音数据获取成本高昂。需要一种能在野外数据上稳定训练、生成自然且难以被检测的合成语音的方法。

**方法创新**：
1. **基于F5-TTS架构**：采用flow matching和diffusion transformer的非自回归TTS基础模型。
2. **指数移动平均（EMA）**：在监督微调中集成EMA，稳定训练、提升泛化能力，缓解过拟合。
3. **双评分提示选择（DPS）**：使用LALM（Qwen2.5-Omni）对音频提示进行质量评分（情感丰富度、表现力、适用性），再使用LLM（Qwen3-30B-A3B）对文本提示进行语义对齐验证，筛选高质量参考。

**实验结果**：
- 开发集：UTMOS 3.20，说话人相似度0.51，WER 8.65%。
- 官方评估：在三个先进SASV系统上取得最佳a-DCF分数（0.1582, 0.5233, 0.2562），表明合成语音最难被检测，自然性和真实性最高。

**一句话评价**：通过EMA稳定微调和双评分提示选择，F5-TTS-DPS在野外TTS任务中实现了高自然度和强欺骗性，在WildSpoof 2026 TTS赛道中取得领先。

---

## 2. Frame-Aligned Fusion of Canary and WavLM for Non-Intrusive Intelligibility Prediction of Hearing-Aid-Processed Speech

**作者**: Kazushi Nakazawa
**链接**: [2605.23619](https://arxiv.org/abs/2605.23619)
**分类**: Speech Intelligibility Prediction / Assistive Hearing | **关键词**: non-intrusive intelligibility prediction, hearing-aid-processed speech, Canary, WavLM, frame-aligned fusion, Clarity Prediction Challenge

## 核心痛点
非侵入式可懂度预测任务中，无法使用干净参考信号，需要利用助听器处理后的语音直接预测听力受损者的理解程度。现有方法多使用预训练模型，但如何有效融合多个编码器（如Canary和WavLM）的互补表征，以及融合时机（帧级还是话语级）尚不明确。

## 方法创新
提出帧对齐融合（Frame-Aligned Fusion），在池化前对WavLM进行可学习步长卷积下采样，使其与Canary较粗的时间轴对齐，实现帧级拼接融合。同时对比了单骨干基线、均匀分数平均、池化后融合、交叉注意力及反向对齐等策略。所有方法在左右耳分别处理，保持双耳信息。

## 实验结果
最佳模型（帧对齐融合+可学习卷积）在CPC3评估集上达到RMSE 24.96±0.06、相关系数0.796±0.001，优于其他融合策略。时间偏移分析表明，精确的帧同步并非必要，粗粒度局部对应是关键。

## 一句话评价
该工作系统性地揭示了在非侵入式可懂度预测中，预训练多编码器的帧级局部融合优于话语级融合，为助听器评估提供了有效归纳偏置。

---

## 3. Word-Level Modeling with Alignment-Aware Acoustic Fusion for Text-Assisted Intelligibility Prediction in Listeners with Hearing Loss

**作者**: Kazushi Nakazawa
**链接**: [2605.23604](https://arxiv.org/abs/2605.23604)
**分类**: Speech Intelligibility Prediction | **关键词**: Speech intelligibility prediction, Whisper, text-assisted prediction, word-level modeling, hearing-impaired listeners, alignment, speech foundation models

## 核心痛点
传统Clarity Prediction Challenge（CPC）中的可懂度预测方法直接将整句话的音频编码后回归一个句子级分数，但句子可懂度本质上是单词识别结果的聚合，导致训练信号的粒度不匹配。

## 方法创新
本文提出**参考条件化的词级正确性建模**：
- 使用冻结的Whisper模型，编码器处理退化语音，解码器以教师强制方式输入规范文本，得到词级解码器状态。
- 增加**对齐感知的局部声学分支**：通过辅助字符级解码器的交叉注意力图动态选择头部，为每个参考词提取对齐的声学特征。
- 增加**全局声学分支**：平均池化编码器状态获取句子级校准信号。
- 将解码器特征、局部声学特征、全局声学特征和听障者严重程度嵌入拼接，通过轻量级分类器预测每个参考词的正确概率，再平均得到句子可懂度。

## 实验结果
在CPC3官方评估集上，解码器基线RMSE=24.92，相关性=0.795；联合融合方法提升至错误词F1=0.778，MCC=0.626，相关性=0.806，RMSE=24.39。Whisper medium模型上观察到一致趋势。

## 一句话评价
本文通过引入词级建模和对齐感知多粒度声学融合，有效弥合了训练信号粒度不匹配问题，显著提升了听力受损者语音可懂度预测的准确性。

---

## 4. A study on weakly-supervised training approaches for phoneme-level pronunciation scoring

**作者**: Jazmín Vidal, Luciana Ferrer
**链接**: [2605.23593](https://arxiv.org/abs/2605.23593)
**分类**: Pronunciation Assessment | **关键词**: weakly-supervised learning, phoneme-level pronunciation scoring, GOPT, Goodness of Pronunciation, computer-assisted pronunciation training

## 核心痛点
音素级发音评分需要大量细粒度的音素标注，数据昂贵且稀缺，制约了计算机辅助发音训练（CAPT）系统的性能。

## 方法创新
提出一种基于GOPT架构的弱监督训练方法：通过将字/句级别的评分作为监督信号，利用平均或注意力池化机制从音素级预测汇总得到高层级分数，从而仅用高层级标签即可训练音素级评分模型。进一步提出两阶段训练：先用句子级标签预训练，再用少量精选的音素级标签微调。

## 实验结果
在Speechocean762数据集上，使用仅句子级标签训练的音素级评分（通过池化）与完全监督（所有层级标签）的结果相当。两阶段训练在仅使用10%音素级标签时性能接近完全监督。

## 一句话评价
巧妙利用高层级标签的弱监督信号，显著降低了对音素级标注的依赖，实现了近乎全监督的性能。

---

## 5. StepAudio 2.5 Technical Report

**作者**: Bin Lin, Bo Zhao, Boyong Wu, Chao Yan, Chen Wu, Cheng Yi, Chengyuan Yao, Daijiao Liu, Fei Tian, Feng Tian, Haiyang Sun, Haoyang Zhang, Jiangjie Zhen, Jinglan Gong, Jun Chen, Li Xie, Peilin Li, Peng Yang, Pengfei Tan, Qingjian Lin, Runze Li, Shenghua Hu, Siyi Zhou, Wenwen Qu, Xiangyu Li, Xiangyu Tony Zhang, Xuerui Yang, Yang Yang, Yechang Huang, Yu Fu, Yuchu Luo, Yuxin Li, Yuxin Zhang, Zhengyan Sheng, Brian Li, Chang Zeng, Changlin Zhang, Chen Geng, Chenghao Dong, Chengli Feng, Dan Zhou, Danni Wan, Di Chen, Die Zhang, Dongqing Pang, Guanglong Yang, Guoqiang Hu, Huangxi Zhu, Jianzheng Gao, Jinghua Liang, Jinmei Wan, Junjie Yuan, Kang An, Lei Lei, Limin Zhong, Lun Cai, Mengqiang Ren, Min Xu, Mingliang Li, Mingxiao Li, Na Wang, Qiang Tong, Qiaoling Huang, Qingfu Du, Rui Wang, Shengchen Zhou, Shi Qiu, Shihao Peng, Shiliang Yang, Siqi Tu, Tianjiao Deng, Ting Xu, Tong Wang, WeiMing Niu, Wuxun Xie, Xianwei Zhang, Xianyu Feng, Xiaojia Liu, Xing Chen, Xiongbin Wu, Yan Wu, Yang Li, Yi Liu, Yifan Zhang, Yile Liu, Yongshen Long, Yu Luo, Yuanhao Ding, Yuhao Wang, Yuhe Yin, Yunfang Xu, Yuxiang Yang, Zhiguo Huang, Zhiyue Wu, Zichao Li, Zichao Zhou, Daxin Jiang, Future Li, Gang Yu, Xiangyu Zhang, Yibo Zhu
**链接**: [2605.23463](https://arxiv.org/abs/2605.23463)
**分类**: Unified Audio-Language Modeling | **关键词**: StepAudio 2.5, unified audio-language modeling, RLHF, ASR, TTS, realtime spoken interaction, multi-token decoding, MTP-5, pretraining, alignment

## 核心痛点
现有统一音频语言模型在自动语音识别(ASR)、文本转语音(TTS)和实时口语交互三项任务上，往往无法达到专用系统的深度。传统级联流水线在语音转文本中间表示时丢失信息，且不同任务目标（如ASR的准确高效转录、TTS的可控表达、实时交互的低延迟与人格一致）难以自然对齐。

## 方法创新
StepAudio 2.5 提出统一的音频语言基础模型，核心思想是：一旦文本和音频共享良好的多模态表示空间，任务差异化便从架构转向操作模式（数据、目标、解码约束）。
- **后训练范式**：从标准监督微调(SFT)扩展到任务定制的强化学习从人类反馈(RLHF)，作为定义复杂优化目标的主要机制。
- **共享骨干**：采用音频编码器-适配器-LLM解码器架构，解码器承载语义、上下文和生成能力。任务专用化通过方向性推理实现：ASR利用可验证的多令牌解码(MTP-5)每次向前步预测6个令牌以加速；TTS通过基于偏好的RLHF和上下文丰富的监督实现可控、富有表现力的合成；Realtime通过生成式奖励建模实现低延迟、人格一致的对话。
- **训练流程**：渐进式预训练，包括对齐阶段（冻结编码器和LLM，仅训练适配器）、多模态训练（文本和语音各800B令牌，分为热身和主训练）、冷却阶段（600B高质量数据，扩展序列长度至32K）。

## 实验结果
在ASR、TTS和Realtime的标准基准上，StepAudio 2.5 取得最先进的结果，超越领先的统一模型和专用系统。

## 一句话评价
StepAudio 2.5 证明了一个统一的音频语言基础模型能够通过任务定制的RLHF和解码策略，在理解、生成和交互三个方向上同时达到专用系统的水平。

---

## 6. Evaluating the Temporal Detection Capability of Integrated Gradients Applied on Sound Classifier

**作者**: Martynas Dumpis, Tuomas Virtanen
**链接**: [2605.23293](https://arxiv.org/abs/2605.23293)
**分类**: Sound Event Detection | **关键词**: Integrated Gradients, Sound Event Detection, Temporal Detection, Explainable AI, Weakly Supervised Learning, Post-hoc Attribution

## 核心痛点

弱监督声音事件检测（SED）中，获取精确的时间边界标注成本高昂。现有可解释性方法（如集成梯度）虽可用于音频分类，但其在时序定位任务中的有效性尚未被系统评估。

## 方法创新

本文系统评估了集成梯度（Integrated Gradients, IG）应用于仅经片段级标签训练的音频分类器时，能否恢复声音事件的时序活动信息。使用合成多声道音频（10类家庭声音，精确的起止时间标注），通过IoU、帧级F1和Pointing Game指标测量IG属性与事件边界的一致性。与弱监督帧级CNN（FW-WS，使用片段级标签）和强监督帧级CNN（FW-SS，使用帧级标签）进行对比。

## 实验结果

在10类家庭声音合成数据集上，IG达到平均IoU=0.39，帧级F1=0.52，Pointing Game准确率=82.6%。作为对比，FW-WS为0.42 IoU、0.55 F1、97.3% PG；FW-SS为0.45 IoU、0.58 F1、97.9% PG。所有方法显著优于随机基线。

## 一句话评价

本文证明即使没有时间监督，后验IG也能捕获有意义的声音事件时序活动模式，其定位性能接近显式生成帧级预测的模型，为弱监督SED的可解释性提供了一种有效替代方案。

---

## 7. UniSRM: A Unified Speech Reward Model for Reasoning-Based Fine-grained Assessment

**作者**: Yuanyuan Wang, Dongchao Yang, Yayue Deng, Zhiyong Wu, Yiwen Guo, Helen Meng, Xixin Wu
**链接**: [2605.23261](https://arxiv.org/abs/2605.23261)
**分类**: Speech Reward Modeling | **关键词**: Speech Reward Model, Fine-grained Assessment, Reasoning, Reinforcement Learning, Unified Evaluation

# UniSRM: A Unified Speech Reward Model for Reasoning-Based Fine-grained Assessment

## 核心痛点
- 当前语音生成评估严重依赖人工MOS评分，成本高、主观、难以规模化。
- 现有自动评估方法（如客观指标WER、SIM）仅覆盖单一维度，缺乏透明度和可解释性。
- 基于AudioLLM的评判模型（如WavReward、SageLM、SpeechJudge）任务覆盖有限（仅语句级或单轮对话），评估维度不完整（如忽略说话人相似性），且推理过程缺乏监督，导致理由与决策不一致。

## 方法创新
- **UniSRM框架**：提出统一的语音奖励模型，支持多维度、可解释的奖励信号，并带有可靠推理。
- **数据集和基准**：构建UniSRM-Data（涵盖语句级质量、情境风格一致性、多轮对话评估等任务）和UniSRM-Bench。
- **两阶段训练**：第一阶段SFT学习多维度分解推理，第二阶段提出Reasoning-Consistent GRPO，在维度级推理过程分配奖励，提升可靠性。
- **多维度评估**：分解为文本保真度、说话人相似度、韵律表现力、自然度等维度，生成推理链后再聚合总分。

## 实验结果（论文片段未提供详细结果，但声称）
- 实验表明UniSRM在多种语音评估任务上输出更可靠、与人类偏好更对齐的判断。

## 一句话评价
UniSRM通过多维度推理分解和一致性强化学习，首次实现了覆盖多种场景的可解释、高可靠语音统一奖励模型。

---

