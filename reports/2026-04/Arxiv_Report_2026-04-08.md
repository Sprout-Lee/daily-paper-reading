# Arxiv Daily Deep Report - 2026-04-08

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 4
---

## 1. Multimodal Deep Learning Method for Real-Time Spatial Room Impulse Response Computing

**作者**: Zhiyu Li, Xinwen Yue, Shenghui Zhao, Jing Wang
**链接**: [2604.05545](https://arxiv.org/abs/2604.05545)
**分类**: Audio Synthesis | **关键词**: Spatial Room Impulse Response, Multimodal Deep Learning, Auralization, Virtual Reality

## 核心痛点

现有VR听觉化方法中，几何声学计算复杂度高，难以实时生成高质量音频；深度学习模型在准确预测低阶反射方面存在局限；现有数据集多样性不足，且RIR类型（如单声道和双耳RIRs）不完全满足VR交互需求。

## 方法创新

提出一个多模态深度学习模型，输入包括场景信息（几何和声学属性）和低阶反射波形，输出空间房间脉冲响应（SRIRs），以降低计算复杂度并便于集成个性化头相关传递函数。构建了包含多样化3D场景和SRIRs的新数据集。模型架构结合GCN-TF编码器、LoR编码器（并行处理波形和Mel-spectrogram）和参数解码器，优化了早期反射和晚期混响的生成。

## 实验结果

在多项客观指标（如MAE、T60、DRR、Mel-spectrogram错误）上，该方法优于基线系统MESH2IR、Listen2Scene和M2PAIR，显示了在实时SRIR计算中的优越性能。数据集特征分布更广泛，提升了模型泛化能力。

## 一句话评价

该研究通过创新多模态输入和SRIR输出，有效解决了VR听觉化中实时音频渲染的挑战，提升了真实感和计算效率。

---

## 2. Active noise cancellation on open-ear smart glasses

**作者**: Kuang Yuan, Freddy Yifei Liu, Tong Xiao, Yiwen Song, Chengyi Shen, Saksham Bhutani, Justin Chan, Swarun Kumar
**链接**: [2604.05519](https://arxiv.org/abs/2604.05519)
**分类**: Audio Enhancement | **关键词**: active noise cancellation, open-ear smart glasses, virtual in-ear sensing, neural network, real-time audio processing

### 核心痛点
传统主动噪声消除（ANC）技术依赖于耳道内的误差麦克风来测量和调整噪声消除效果，但开放式耳机智能眼镜无法使用这种设计，因为它们不能密封耳道，导致在嘈杂环境中音频质量下降。
### 方法创新
提出首个实时ANC系统，通过分布在眼镜框架上的八个MEMS麦克风阵列捕获环境噪声，利用神经网络进行虚拟耳内感知来估计噪声在耳道中的传播。系统采用双管道架构：CPU运行神经网络（每200毫秒更新一次滤波器系数），DSP实时生成抗噪声信号（延迟113微秒）。方法还支持用户校准以优化性能。
### 实验结果
在100-1000 Hz频率范围内的8个移动环境中进行用户研究，使用自定义3D打印原型眼镜，实现平均噪声减少：无校准时9.6 dB，用户校准时11.2 dB。系统能有效处理动态声学条件，适用于真实世界穿戴场景。
### 一句话评价
这篇论文首次在开放式耳机智能眼镜上实现了实时主动噪声消除，通过创新性的虚拟耳内感知和低延迟处理，为穿戴式音频增强和未来智能交互奠定了技术基础。

---

## 3. Exploring Speech Foundation Models for Speaker Diarization Across Lifespan

**作者**: Anfeng Xu, Tiantian Feng, Shrikanth Narayanan
**链接**: [2604.05201](https://arxiv.org/abs/2604.05201)
**分类**: Speaker Diarization | **关键词**: Speaker Diarization, Speech Foundation Models, Age-related Domain Shift

# 论文总结：Exploring Speech Foundation Models for Speaker Diarization Across Lifespan

## 核心痛点
- 现有的说话人日记化（Speaker Diarization）系统主要基于成人语音数据（如25-60岁年龄组）训练和评估，但实际应用常涉及儿童和老年语音，这些语音存在年龄相关的声学差异（如音高、发音模式、语速变化），导致模型在跨年龄组应用时性能显著下降。
- 语音基础模型（如Whisper和WavLM）在多种语音任务中表现出强迁移能力，但它们在年龄相关领域转移下的说话人日记化效果尚未系统探索。

## 方法创新
- 提出了一个统一的端到端神经日记化框架（EEND-VC），集成语音基础模型作为编码器，以评估跨年龄组的鲁棒性。
- 评估三种实际场景：
  1. **零样本跨年龄推理**：仅用成人数据训练，直接应用于儿童和老年语音。
  2. **联合多年龄训练**：结合成人、儿童和老年数据集进行训练。
  3. **领域特定适应**：在成人模型基础上，针对儿童或老年数据微调。
- 实验覆盖成人会议数据集（如AMI、AISHELL-4、AliMeeting）和年龄多样化数据集（如Playlogue儿童数据和SeniorTalk老年数据）。

## 实验结果
- **零样本推理**：模型在儿童和老年语音上性能显著下降（例如，在Playlogue数据集上误字率（DER）高达65%以上）。
- **联合多年龄训练**：提高了在儿童和老年语音上的鲁棒性，同时不损害成人语音性能，甚至在某些情况下提升。
- **领域适应**：针对特定年龄组微调进一步改进性能，特别是使用Whisper编码器时。例如，Whisper-Medium模型在老年数据上适应后误字率相对下降45.8%。
- 结果表明，Whisper编码器从领域适应中受益较大，而WavLM模型在跨年龄泛化中表现更稳健。

## 一句话评价
本文系统性评估了语音基础模型在说话人日记化中的跨年龄泛化能力，为应对年龄多样性提供了实用见解和基准，推动了鲁棒语音处理的发展。

---

## 4. Generalizable Audio-Visual Navigation via Binaural Difference Attention and Action Transition Prediction

**作者**: Jia Li, Yinfeng Yu
**链接**: [2604.05007](https://arxiv.org/abs/2604.05007)
**分类**: Audio-Visual Navigation | **关键词**: Audio-Visual Navigation, Binaural Difference Attention, Action Transition Prediction, Generalization, Reinforcement Learning

### 核心痛点
现有音频视觉导航（AVN）方法在未见声音类别和环境中泛化能力有限，主要问题包括对声音语义特征的过拟合、对训练环境动态和几何的依赖，导致在分布外场景下性能下降，如方向推断不稳定和导航轨迹振荡。
### 方法创新
提出 BDATP 框架，包括两个核心组件：Binaural Difference Attention (BDA) 模块，通过显式建模双耳差异来增强空间方向感知，减少对语义类别的依赖；Action Transition Prediction (ATP) 任务，作为辅助正则化项，通过预测动作转移来促进跨环境的策略一致性，缓解过拟合问题。该框架可集成到主流 AVN 基线中，共同优化感知和策略学习。
### 实验结果
在 Replica 和 Matterport3D 数据集上的实验表明，BDATP 显著提升了性能，特别是在挑战性的零样本泛化设置中。例如，在 Replica 数据集的未见声音类别上，成功率达到最高 21.6% 的绝对提升（例如，AV-WaN + BDATP 达 70.7%），并展示了跨不同导航架构的稳健性。
### 一句话评价
BDATP 框架通过强调空间感知和策略正则化，有效地解决了 AVN 中的泛化问题，为未见场景下的音频视觉导航提供了创新解决方案。

---

