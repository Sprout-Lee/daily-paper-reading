# Arxiv Daily Deep Report - 2026-04-29

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 8
---

## 1. Step-Audio-R1.5 Technical Report

**作者**: Yuxin Zhang, Xiangyu Tony Zhang, Daijiao Liu, Fei Tian, Yayue Deng, Jun Chen, Qingjian Lin, Haoyang Zhang, Yuxin Li, Jinglan Gong, Yechang Huang, Liang Zhao, Chengyuan Yao, Hexin Liu, Eng Siong Chng, Xuerui Yang, Gang Yu, Xiangyu Zhang, Daxin Jiang
**链接**: [2604.25719](https://arxiv.org/abs/2604.25719)
**分类**: Large Audio Language Models | **关键词**: Chain-of-Thought, Reinforcement Learning with Verified Rewards, Reinforcement Learning from Human Feedback, Audio Reasoning, Multi-turn Spoken Dialogue, Verifiable Reward Trap

## 核心痛点
当前主流的音频推理模型依赖强化学习与验证奖励（RLVR），但RLVR仅优化离散标签的正确性，导致模型在真实对话中丧失自然度、情感连续性和沉浸感，沦为“答录机”。作者将此现象称为“可验证奖励陷阱”。

## 方法创新
提出Step-Audio-R1.5，首次将基于人类反馈的强化学习（RLHF）系统性地引入音频推理。通过训练基于人类偏好判断的奖励模型，统一优化正确性、流畅性和情感共鸣，跳出奖励陷阱。架构采用Qwen2音频编码器（25Hz，冻结）、2倍下采样适配器（12.5Hz）和Qwen2.5 32B LLM解码器。训练分为三阶段：音频中心中期训练（强化音频推理）、冷启动SFT（优化多轮对话行为）、基于规则生成奖励模型的RLHF（联合优化显式约束与偏好驱动目标）。

## 实验结果
在语音转文本基准（如AudioMultiChallenge、Step-Caption等）上，Step-Audio-R1.5显著优于前代，并与Gemini 3 Pro等商业系统竞争。多轮对话能力在自然交互维度上大幅提升。

## 一句话评价
Step-Audio-R1.5通过RLHF解决了音频RLVR的“可验证奖励陷阱”，在保持推理准确性的同时大幅改善了对话自然度与用户体验。

---

## 2. UNet-Based Fusion and Exponential Moving Average Adaptation for Noise-Robust Speaker Recognition

**作者**: Chong-Xin Gan, Peter Bell, Man-Wai Mak, Zhe Li, Zezhong Jin, Zilong Huang, Kong Aik Lee
**链接**: [2604.25624](https://arxiv.org/abs/2604.25624)
**分类**: Speaker Recognition | **关键词**: Speaker Recognition, Speech Enhancement, Exponential Moving Average, UNet Feature Fusion, Noise Robustness

## 核心痛点
传统的语音增强+说话人识别级联方法存在两个问题：1) 预训练的语音增强模型可能引入伪影，且未充分利用噪声语音中的说话人信息；2) 联合训练时，说话人编码器容易过拟合，且无法平滑地从干净语音过渡到噪声环境。

## 方法创新
1. **UNet融合模块**：将噪声语音与多个预训练增强模型（如BSRNN和DEMUCS）的输出在频谱层面堆叠，通过UNet进行非线性融合，生成鲁棒的融合表示，避免线性组合的信息损失。
2. **指数移动平均（EMA）策略**：使用预训练在干净语音上的说话人编码器初始化，并通过EMA动态更新参数，实现从干净到噪声环境的平滑过渡，防止灾难性遗忘。

## 实验结果
在多个噪声测试集上，UF-EMA方法优于现有方法（如单独训练、联合训练、观察添加等），展示了优越的噪声鲁棒性。

## 一句话评价
提出了一种结合UNet融合与EMA更新的噪声鲁棒说话人识别框架，有效利用了预训练增强模型的多源信息并缓解了过拟合问题。

---

## 3. Walking Through Uncertainty: An Empirical Study of Uncertainty Estimation for Audio-Aware Large Language Models

**作者**: Chun-Yi Kuan, Wei-Ping Huang, Hung-yi Lee
**链接**: [2604.25591](https://arxiv.org/abs/2604.25591)
**分类**: Uncertainty Estimation in Audio-Aware LLMs | **关键词**: uncertainty estimation, audio-aware large language models, semantic entropy, hallucination detection, unanswerable question answering

# 论文总结

## 核心痛点
音频感知大语言模型（ALLMs）在音频理解与推理任务中表现优异，但仍频繁产生幻觉或过度自信的输出。尽管不确定性估计在纯文本LLMs中已有广泛研究，但在ALLMs中尚未被系统性探索，音频条件生成引入了感知模糊性和跨模态 grounding 等额外挑战。

## 方法创新
本文首次系统性地实证研究了ALLMs中的不确定性估计。基准测试了五种代表性方法：预测熵（Predictive Entropy）、长度归一化熵（Length-Normalized Entropy）、语义熵（Semantic Entropy）、离散语义熵（Discrete Semantic Entropy）和 P(True)。采用两阶段协议：先用低温解码获得预测答案，再通过采样估计不确定性。

## 实验结果
在通用音频理解与推理基准上，语义级和验证性方法（语义熵、P(True)）一致优于 token 级基线（预测熵、长度归一化熵）。在可信度导向基准（幻觉检测、不可回答问题）上，方法相对有效性变得高度依赖模型和任务，表明通用推理基准的结论不能直接迁移。此外，不确定性驱动的自适应推理作为下游应用进行了探索，但其效果取决于替代推理策略本身是否有益。

## 一句话评价
本文填补了ALLMs不确定性估计的空白，揭示了语义级方法在通用场景的优势及其在可信场景的局限性。

---

## 4. ASAP: An Azimuth-Priority Strip-Based Search Approach to Planar Microphone Array DOA Estimation in 3D

**作者**: Ming Huang, Shuting Xu, Leying Yang, Huanzhang Hu, Yujie Zhang, Jiang Wang, Yu Liu, Hao Zhao, He Kong
**链接**: [2604.25387](https://arxiv.org/abs/2604.25387)
**分类**: Direction-of-Arrival Estimation | **关键词**: DOA estimation, SRP-PHAT, planar arrays, sound source localization, region contraction

# ASAP: 平面麦克风阵列3D DOA估计的方位优先带状搜索方法

## 核心痛点
- 传统的SRP-PHAT方法在3D场景下需要在数千个候选方向上评估，计算开销大，难以在资源受限平台上实时运行。
- 平面麦克风阵列的仰角估计通常比方位角估计更不可靠，现有方法（如CFRC）未充分利用这一特性。

## 方法创新
- 提出ASAP方法，将3D搜索分解为两个阶段：
  - **阶段1（方位优先带状搜索）**：在方位角带状区域内执行粗到细的区域收缩（CFRC-style），并通过球冠过滤保留多个峰值，锁定方位角。
  - **阶段2（一维仰角细化）**：沿大圆路径在候选点之间进行一维搜索，细化仰角估计。
- 两种细化策略：Meridian-Centered (MC) 和 Between-Points (BP)，后者利用球面线性插值（SLERP）在两点间生成候选方向。

## 实验结果
- 仿真实验（3751个点）：ASAP（BP）在无噪声、3.09 dB噪声、1.5 dB噪声条件下，RMSE均低于或等于全网格SRP-PHAT和CFRC。
- 最高网格分辨率下，ASAP相比CFRC减少了13.56%的运行时间和5.87%的RMSE。
- 真实世界实验（8麦克风UCA）：ASAP比CFRC快13.98%，RMSE低4.33%。

## 一句话评价
ASAP通过利用平面阵列的方位优先特性，显著提升了3D DOA估计的效率和精度，适用于实时声源定位应用。

---

## 5. Cross-Linguistic Rhythmic and Spectral Feature-Based Analysis of Nyishi and Adi: Two Under-Resourced Languages of Arunachal Pradesh

**作者**: Deepshikha Gogoi, Parismita Gogoi, Yang Saring
**链接**: [2604.25309](https://arxiv.org/abs/2604.25309)
**分类**: Speech Rhythm Analysis | **关键词**: Under-resourced languages, Rhythm Formant Analysis, Amplitude Modulation, Tani languages, MFCC, DCT

# 核心痛点
Nyishi和Adi是印度阿鲁纳恰尔邦的两种低资源语言，属于Tani语支。此前缺乏系统性声学-韵律分析，尤其是在节奏方面。传统基于间隔的节奏度量方法存在局限性，且难以用于语言区分。

# 方法创新
本文采用基于幅度调制（AM）低频（LF）频谱分析的节奏共振峰分析（RFA），直接从语音信号的包络中提取节奏特征（NDP、MFDP、VFDP），无需人工分割。同时提取DCT系数和MFCC表征频谱调制和整体频谱组织。通过统计建模和机器学习（SVM、MLP）评估节奏和频谱特征在语言区分中的层次性。

# 实验结果
- 仅使用节奏特征（RFA）的分类准确率约84-85%。
- 融合MFCC后，SVM准确率达90.9%，MLP达93.96%。
- 统计结果显示节奏特征表现出一致但温和的分离（Nyishi具有更高的主调制频率和更大的离散度），而频谱特征反映更精细的音位差异，形成层次化区分模式。

# 一句话评价
本文为低资源语言内部的声学区分提供了统一的信号处理框架，验证了节奏和频谱特征在互补水平上编码语言差异的假设。

---

## 6. Praxy Voice: Voice-Prompt Recovery + BUPS for Commercial-Class Indic TTS from a Frozen Non-Indic Base at Zero Commercial-Training-Data Cost

**作者**: Venkata Pushpak Teja Menta
**链接**: [2604.25441](https://arxiv.org/abs/2604.25441)
**分类**: Text-to-Speech | **关键词**: text-to-speech, Indic languages, low-resource TTS, LoRA, voice cloning, Brahmic script processing, romanisation, open-source TTS

## 核心痛点
商业级Indic TTS系统需要大量GPU资源和商业数据，开源多语言基座（如Chatterbox）不支持Telugu/Tamil，且输出质量远逊于商业系统。

## 方法创新
1. **BUPS (Brahmic Unified Phoneme Space)**：将Devanagari、Telugu等Brahmic脚本确定性罗马化为ISO-15919拉丁字符串，使得Chatterbox的拉丁分词器可以处理。
2. **LoRA适配器**：仅在Chatterbox的文本预测器（t3）上训练LoRA（7.86M参数，占0.97%），使用BUPS预处理数据并伪装成Hindi语言ID，冻结声学解码器和语音编码器。
3. **推理时语音提示恢复**：提供8-11秒同语言参考音频，配合特定采样参数（exaggeration 0.7, temperature 0.6, min_p 0.1，称为Config B），无需训练声学解码器即可恢复商业级输出。

## 实验结果
- Telugu：retroflex collapse 26.7%（商业最佳Sarvam Bulbul 33.3%），排名第一。
- Tamil：zha collapse 71%（商业系统86%），最显著提升。
- Hindi：LLM-WER 0.025（与Cartesia Sonic-3持平）。
- 代码混合场景：IndicF5 + 原生脚本转写预处理器，LLM-WER从0.80-0.85降至0.14-0.27。

## 一句话评价
本文以极小代价（无商业训练数据、仅微调0.97%参数）将不支持Telugu/Tamil的冻结多语言TTS基座提升至商业级，并开源LoRA权重和推理代码。

---

## 7. ML-SAN: Multi-Level Speaker-Adaptive Network for Emotion Recognition in Conversations

**作者**: Kexue Wang, Yinfeng Yu, Liejun Wang
**链接**: [2604.25383](https://arxiv.org/abs/2604.25383)
**分类**: Emotion Recognition in Conversations | **关键词**: multimodal sentiment recognition, emotional expression differences, multi-level speaker adaptive network, speaker identity confusion

## 核心痛点
现有对话情感识别方法忽视个体表达差异，将不同说话人视为可互换实体，导致特征错配和融合失效，尤其在多轮对话中识别效果差。

## 方法创新
提出多级说话人自适应网络（ML-SAN），通过三阶段自适应过程：
- **输入层校准（Input-level Calibration）**：使用特征级线性调制（FiLM）将原始音视频特征调整至与说话人无关的中性空间。
- **交互层门控（Interaction-level Gating）**：基于说话人身份信息动态重新调整每个模态（如语音或面部特征）的信任度。
- **输出层正则化（Output-level Regularization）**：在潜在空间中保持说话人特征的一致性，引入辅助分类任务。

## 实验结果
在MELD和IEMOCAP数据集上，ML-SAN的加权F1分数分别达到67.73%和73.28%，优于所有基线（如MultiEMO提升1.39%和1.26%），消融实验验证了各组件的有效性。

## 一句话评价
通过多级说话人自适应机制，有效解决了说话人身份混淆问题，显著提升多模态对话情感识别的鲁棒性和准确性。

---

## 8. Korean aegyo speech shows systematic F1 increase to signal childlike qualities

**作者**: Ji-eun Kim, Volker Dellwo
**链接**: [2604.25133](https://arxiv.org/abs/2604.25133)
**分类**: 语音学（社会语音学/声学语音学） | **关键词**: aegyo, vowel space, formant frequency, childlike speech, Korean, voice style, F1 increase

### 核心痛点
现有研究对韩国撒娇语（aegyo）的语音特征关注不足，尤其缺乏对元音空间的系统性分析，而元音空间是构建孩童化语体的重要声学维度。

### 方法创新
- 招募12名首尔韩语母语者（6男6女），在同一脚本下分别以撒娇和非撒娇风格朗读。
- 采用标准共振峰分析，提取8个单元音的平均F1、F2，并计算角元音三角形（/i, a, u/）和全元音凸包面积及质心。
- 通过线性混合效应模型检验风格对元音空间面积、质心F1/F2及单个元音共振峰的影响。

### 实验结果
- **F1显著增加**：撒娇语中所有元音的F1均显著上升（平均提升约43 Hz），表明元音整体降低（模仿儿童较短的声道）。
- **角元音空间扩大且前移**：角元音三角形面积显著扩大（+17,716 Hz²），且质心F2显著增加（前移）。
- **全元音空间扩大但无显著前后移动**：全元音凸包面积显著扩大（+46,454 Hz²），但F2质心无显著变化，说明前后移动仅局限于前元音。
- 个别元音（如 /i/）F2显著增加（前移），后元音（如 /u/）F2无显著变化。

### 一句话评价
该研究首次揭示韩国撒娇语通过系统性地增加F1（元音降低）来模仿儿童声学特征，并伴随前元音选择性前移，为语体中介的语音风格化提供了量化证据。

---

