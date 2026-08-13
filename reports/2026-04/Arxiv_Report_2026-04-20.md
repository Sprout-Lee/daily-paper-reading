# Arxiv Daily Deep Report - 2026-04-20

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 2
---

## 1. ArtifactNet: Detecting AI-Generated Music via Forensic Residual Physics

**作者**: Heewon Oh
**链接**: [2604.16254](https://arxiv.org/abs/2604.16254)
**分类**: Audio Forensics for AI-Generated Content | **关键词**: AI-generated music detection, forensic physics, residual analysis, neural audio codecs, ArtifactNet

**核心痛点**: AI生成音乐在流媒体平台泛滥，现有检测方法（如表示学习和自编码器指纹识别）在未见生成器上泛化能力差，且受音频编解码器和流派分布影响。

**方法创新**: 提出ArtifactNet框架，将问题重构为法医物理学，专注于提取神经音频编解码器（如RVQ）留下的不可逆残差伪影。使用ArtifactUNet（3.6M参数）从幅度谱中提取残差，通过HPSS分解为7通道法医特征，并由紧凑CNN（0.4M参数）分类。引入代码感知训练以提高跨编解码器鲁棒性。

**实验结果**: 在ArtifactBench基准（6,183轨道，22个生成器）的未见测试集（n=2,263）上，ArtifactNet达到F1=0.9829，FPR=1.49%，优于CLAM（F1=0.7576）和SpecTTTra（F1=0.7713）。参数效率高，总参数4.0M，比CLAM少49倍，比SpecTTTra少4.8倍。代码感知训练将跨编解码器概率漂移减少83%。

**一句话评价**: ArtifactNet通过法医残差物理学，提供了一个轻量级、高效且泛化能力强的AI音乐检测范式。

---

## 2. Qwen3.5-Omni Technical Report

**作者**: Qwen Team
**链接**: [2604.15804](https://arxiv.org/abs/2604.15804)
**分类**: Omnimodal Large Language Models | **关键词**: Qwen3.5-Omni, Omni-modality, ARIA, Hybrid Attention MoE, Audio-Visual Understanding, Multilingual Speech Generation

### 核心痛点
现有全模态系统主要局限于被动感知-响应范式，缺乏可扩展的代理行为、实时交互、自主工具利用和跨模态推理能力，这些是实际部署的关键障碍。

### 方法创新
Qwen3.5-Omni引入多项关键技术升级：
- 采用混合注意力MoE（Mixture-of-Experts）架构，在Thinker和Talker中实现高效推理。
- 支持256k上下文长度，可处理长达10小时音频和400秒720P视频（以1 FPS）。
- 引入ARIA（Adaptive Rate Interleave Alignment）技术，动态对齐文本和语音单元，显著改善流式语音合成的稳定性和自然度。
- 扩展多语言支持至113种语言用于语音识别和36种用于语音合成。
- 新增能力：可控音频-视觉字幕（生成结构化描述和自动场景分割）、实时交互（包括语音中断识别和零样本语音克隆）、原生全模态代理行为（如自主WebSearch和音频-视觉Vibe编码）。

### 实验结果
Qwen3.5-Omni-Plus在215个音频和音频-视觉理解、推理和交互子任务中达到SOTA（State-of-the-Art），在关键音频任务中超越Gemini-3.1 Pro，整体音频-视觉理解与之匹配。模型在文本和视觉模态上保持SOTA性能，无退化。

### 一句话评价
Qwen3.5-Omni通过创新架构和大规模多模态训练，实现了高效的全模态理解和生成，在音频-视觉交互和实时应用中表现卓越，推动了AI向更自然、代理式的多模态系统发展。

---

