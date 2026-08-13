# Arxiv Daily Deep Report - 2026-04-16

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 4
---

## 1. SpeakerRPL v2: Robust Open-set Speaker Identification through Enhanced Few-shot Foundation Tuning and Model Fusion

**作者**: Zhiyong Chen, Shuhang Wu, Yingjie Duan, Xinkang Xu, Xinhui Hu
**链接**: [2604.13605](https://arxiv.org/abs/2604.13605)
**分类**: Open-set Speaker Identification | **关键词**: open-set speaker identification, few-shot learning, model fusion, reciprocal points learning, logit normalization, adaptive anchor learning

# 论文总结: SpeakerRPL v2

## 核心痛点
该论文旨在解决开放集说话人识别中的关键挑战：在有限 enrollment 数据下，提高基础模型的利用效率，增强对未见说话人的鲁棒性，并减少 few-shot 调优过程中的随机性，以提升泛化能力。

## 方法创新
- **增强的开放集学习目标**：结合 reciprocal points learning、logit normalization (LogitNorm) 和 adaptive anchor learning，以优化目标说话人表示并提升鲁棒性。
- **模型融合策略**：通过分数级平均融合多个适配器模型，减少 few-shot 调优的随机性，稳定训练过程。
- **模型选择方法**：基于中心点 (CPs) 和 reciprocal points (RPs) 的相似性矩阵特征值分布，自动选择最优候选模型进行融合，确保性能最优。

## 实验结果
在 VoxCeleb、3D-Speaker 和 ESD 等数据集上进行评估：
- 在 Vox1-O–like 测试集上，将等错误率 (EER) 从 1.28% 降低至 0.09%，相对减少约 93%。
- 在其他数据集上，EER 和 minDCF 指标均有显著改善，OSCR 和 ACC 也得到提升，证明了方法的有效性和泛化能力。

## 一句话评价
SpeakerRPL v2 通过集成多种学习目标和模型融合策略，显著提高了开放集说话人识别的鲁棒性和性能，是该领域的一个重要进展。

---

## 2. Few-Shot and Pseudo-Label Guided Speech Quality Evaluation with Large Language Models

**作者**: Ryandhimas E. Zezario, Dyah A. M. G. Wisnu, Szu-Wei Fu, Sabato Marco Siniscalchi, Hsin-Min Wang, Yu Tsao
**链接**: [2604.13528](https://arxiv.org/abs/2604.13528)
**分类**: Speech Quality Assessment | **关键词**: speech quality, large language models, pseudo-label, few-shot learning, GatherMOS

# 论文总结：Few-Shot and Pseudo-Label Guided Speech Quality Evaluation with Large Language Models

## 核心痛点
- 人类语音质量评估虽为黄金标准，但耗时昂贵，需大量听众以获取可靠分数。
- 深度学习模型需要大量训练数据以实现稳健性能，限制了在低资源场景下的应用。
- 现有大型语言模型（LLMs）如ChatGPT在直接处理音频时存在困难，且缺乏集成声学特征和辅助预测器的机制，导致鲁棒性不足。

## 方法创新
- 提出GatherMOS框架：利用LLMs（如GPT-5）作为元评估器，通过结构化提示集成轻量级声学描述符（如RMS、ZCR、MFCC）和伪标签（来自DNSMOS和VQScore），以预测感知平均意见分数（MOS）。
- 支持零样本和少样本上下文学习设置：零样本GatherMOS依赖基本特征和伪标签，少样本版本额外加入标记示例作为上下文指导，提升在匹配条件下的性能。
- 框架设计避免模型参数更新，仅通过输入上下文进行推理，提高了实用性和计算效率。

## 实验结果
- 在VoiceBank-DEMAND数据集上评估：使用线性相关系数（LCC）和斯皮尔曼等级相关系数（SRCC）作为指标。
- 零样本GatherMOS（GatherMOS-ZS）在有限数据条件下，性能优于基线方法DNSMOS、VQScore、朴素平均（NaiveEnsemble）以及基于学习的模型（CNN-BLSTM和MOS-SSL）。
- 少样本GatherMOS（GatherMOS-FS）在测试条件与支持样本匹配时，性能显著提升（如SRCC达0.8473），但可能因样本不匹配导致泛化能力下降。
- 实验还表明，加入更丰富的声学特征（如MFCC和频谱图统计）能进一步改进零样本性能。

## 一句话评价
GatherMOS展示了LLMs作为元评估器在语音质量评估中的潜力，通过集成多源信息实现了低依赖标注数据的可扩展评估，为未来研究提供了实用策略。

---

## 3. Classical Machine Learning Baselines for Deepfake Audio Detection on the Fake-or-Real Dataset

**作者**: Faheem Ahmad, Ajan Ahmed, Masudul Imtiaz
**链接**: [2604.13400](https://arxiv.org/abs/2604.13400)
**分类**: Deepfake Audio Detection | **关键词**: deepfake audio detection, machine learning, acoustic features, speech synthesis, Fake-or-Real dataset

## 核心痛点
深度学习技术生成了高度逼真的合成语音，导致欺诈、冒充和虚假信息等安全威胁。当前深度伪造音频检测方法主要依赖深度神经网络，虽然性能强，但计算资源需求高且缺乏可解释性，难以揭示判别声学线索。

## 方法创新
本文采用经典机器学习方法，建立可解释的基线。关键创新包括：提取韵律（如音高变异性）、音质（如抖动和颤动）和频谱（如频谱质心和带宽）特征；使用ANOVA进行特征选择；训练多种分类器（逻辑回归、LDA、QDA、高斯朴素贝叶斯、SVM、GMM）；并在高保真（44.1 kHz）和电话质量（16 kHz）音频条件下评估。

## 实验结果
在Fake-or-Real数据集上，RBF SVM模型表现最佳：测试准确率约93%，EER约7%（44.1 kHz和16 kHz条件均如此）。线性模型（如逻辑回归、线性SVM）准确率约75%。特征分析表明，音高变异性（如f0_std_v）和频谱丰富度（如频谱质心、带宽）是关键判别线索。统计分析确认了模型性能的显著差异。

## 一句话评价
该论文提供了一个强大、可解释的基线，有助于未来深度伪造音频检测器的开发和声学线索理解。

---

## 4. ProSDD: Learning Prosodic Representations for Speech Deepfake Detection against Expressive and Emotional Attacks

**作者**: Aurosweta Mahapatra, Ismail Rasim Ulgen, Kong Aik Lee, Nicholas Andrews, Berrak Sisman
**链接**: [2604.13229](https://arxiv.org/abs/2604.13229)
**分类**: Speech Deepfake Detection | **关键词**: Speech Deepfake Detection, Prosody, Emotional Attacks

## 核心痛点
当前语音深度伪造检测(SDD)系统在标准基准数据集（如ASVspoof）上表现良好，但在面对表达性和情感性欺骗攻击时泛化能力不足。这些系统往往过度依赖欺骗数据集中特定的伪影，而非学习自然语音的可转移线索，如韵律变化，导致在分布偏移下性能下降。人类则通过内化真实语音的韵律和说话人模式来检测合成语音的偏差。

## 方法创新
论文提出ProSDD，一个两阶段框架：第一阶段（仅使用真实语音）通过监督掩码预测学习说话人条件下的韵律表示，基于音高、语音活动和能量提取的结构化嵌入；第二阶段（使用真实和欺骗语音）联合优化欺骗分类和韵律学习，通过辅助损失保留韵律建模。该框架使用轻量级分类头，避免复杂架构依赖，强调通过韵律表示增强模型鲁棒性。

## 实验结果
ProSDD在多个数据集上显著提升性能：在ASVspoof 2024上，等错误率(EER)从25.43%降低到16.14%（基于2019训练）和从39.62%降低到7.38%（基于2024训练）；在EmoFake和EmoSpoof-TTS上实现约50%的相对性能提升。结果表明，该方法在标准基准和情感性攻击下均具有优越泛化能力。

## 一句话评价
ProSDD通过结合韵律表示和两阶段训练，有效增强了语音深度伪造检测对表达性和情感性攻击的鲁棒性，同时保持标准基准上的竞争力，为领域提供了新的泛化策略。

---

