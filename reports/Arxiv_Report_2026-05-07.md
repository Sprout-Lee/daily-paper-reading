# Arxiv Daily Deep Report - 2026-05-07

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 2
---

## 1. Spatial-Magnifier: Spatial upsampling for multichannel speech enhancement

**作者**: Dongheon Lee, Ashutosh Pandey, Sanjeel Parekh, Daniel Wong, Jacob Donley, Buye Xu, Juan Azcarreta
**链接**: [2605.04749](https://arxiv.org/abs/2605.04749)
**分类**: Audio Enhancement | **关键词**: Spatial upsampling, multichannel speech enhancement, virtual microphone estimation, generative adversarial network, spatial audio representation learning

# Spatial-Magnifier: Spatial Upsampling for Multichannel Speech Enhancement

## 核心痛点
- 多通道语音增强算法性能随麦克风数量增加而提升，但消费级设备（如AR眼镜、耳机）受物理空间限制，无法集成大规模麦克风阵列。
- 现有虚拟麦克风估计方法（Neural-VME）多沿用标准语音增强架构，缺乏针对空间上采样的专门设计，且未充分研究如何最优地利用虚拟麦克风信号来调节下游语音任务。

## 方法创新
1. **Spatial-Magnifier**：基于生成对抗网络（GAN）的虚拟麦克风生成模型，包含两个核心模块：
   - **Selection Module (SM)**：通过点卷积和Mish激活实现通道级门控机制，自适应提取相关空间特征。
   - **Dynamic Channel Allocation (DCA)**：利用动态卷积计算通道注意力，自适应调整空间滤波器重要性，实现高效信息压缩。
2. **Spatial Audio Representation Learning (SARL)**：两种策略将虚拟麦克风信息融入下游MC-SE模型：
   - **SARL-Signal (SARL-S)**：在信号级直接拼接虚拟麦克风波形。
   - **SARL-Feature (SARL-F)**：在特征级融合虚拟麦克风的隐空间表示，作为空间正则化项。
3. 首次提出**虚拟麦克风语音增强 (VM-SE)** 任务，无需波束成形后端即可直接提升端到端模型性能。

## 实验结果
- 在DNS挑战数据集和模拟空间数据上评估（包括全向SE和视场SE任务）。
- 相比现有Neural-VME基线（如VM-BF），Spatial-Magnifier+SARL在SI-SDR、PESQ、STOI等指标上显著提升，且计算成本更低。
- 接近全麦克风（6通道）的oracle性能，验证了空间上采样的有效性。

## 一句话评价
提出了一种专为多通道语音增强设计的空间上采样GAN模型及特征调节框架，有效突破了麦克风数量限制，性能接近理想全阵列水平。

---

## 2. JASTIN: Aligning LLMs for Zero-Shot Audio and Speech Evaluation via Natural Language Instructions

**作者**: Leying Zhang, Bowen Shi, Haibin Wu, Bach Viet Do, Yanmin Qian
**链接**: [2605.04505](https://arxiv.org/abs/2605.04505)
**分类**: Audio and Speech Evaluation | **关键词**: Large Language Model, Zero-Shot, Instruction-Driven, Audio Evaluation, Speech Evaluation, LLM-as-a-Judge

## 论文总结

**核心痛点:**
1. 传统客观指标（如PESQ、STOI）领域通用性差，无法跨语音、音乐、音效统一评估。
2. 通用多模态大模型（MLLM，如GPT-4o）在专业音频评估中表现不稳定。
3. 专用LLM评估模型缺乏零样本泛化能力和指令灵活性，对提示词变化敏感，评分尺度固定。

**方法创新:**
- 提出JASTIN框架，将音频评估转化为自指令推理任务，结合冻结的音频编码器、可训练的音频适配器和微调的LLM骨干。
- 引入四维数据准备流水线：多源、多任务（24个任务，包含人工标注、伪标签、代理任务）、多校准（支持不同评分尺度）、多描述（LLM改写指令模板）。
- 通过自指令训练实现语义敏感性与词汇鲁棒性的平衡：对评估规则和校准尺度的变化自适应，对纯措辞变化保持评分一致。

**实验结果:**
- 在语音、声音、音乐及域外评估任务上，Pearson和Spearman相关系数与人类主观评分达到SOTA，且无需任务特定重训练。
- 一致优于通用MLLM。

**一句话评价:**
JASTIN是一个统一、指令驱动的零样本音频评估框架，通过精心设计的训练数据和架构实现了跨域泛化与指令鲁棒性。

---

