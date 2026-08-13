# Arxiv Daily Deep Report - 2026-08-07

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 5
---

## 1. EG-VAE: A Unified Framework for Electric Guitar Tone Transfer and Removal

**作者**: Yen-Tung Yeh, Yun-Ning (Amy)Hung, Yi-Hsuan Yang
**链接**: [2608.05513](https://arxiv.org/abs/2608.05513)
**分类**: Audio Effects Modeling | **关键词**: Electric guitar tone transfer, Tone removal, Variational autoencoder, Content-tone disentanglement, Audio effects, Guitar signal chain

## 核心痛点
- 电吉他音色转移（EGTT）和音色去除（EGTR）是吉他音色建模中的两个基础任务，但现有方法通常独立处理，忽略了两者本质上是对同一音色属性的相反操作。
- EGTT的现有方法假设输入为干信号或仅含轻处理，无法处理已经带有未知效果链的湿信号；EGTR现有方法只针对有限的简化效果（如硬削波、部分失真），无法覆盖完整的吉他信号链（含调制、空间效果等）。
- 两者共享的根本问题在于缺乏统一的表征学习，导致任务之间割裂，且泛化到未见音色时效果不佳。

## 方法创新
- **EG-VAE统一框架**：提出基于变分自编码器（VAE）的框架，将湿录音分解为帧级内容表征和全局音色表征，实现EGTT与EGTR的联合建模。
- **音色掩蔽（Tone Masking）**：在解码器输入中移除音色信息，仅依赖内容表征重构干信号。该机制既定义了EGTR（掩蔽前向传播直接输出干信号），也强制内容表征不携带音色信息，抑制了表征泄漏。
- **两阶段训练**：第一阶段通过音色掩蔽学习内容-音色解耦；第二阶段采用变分采样和音频效果增强，塑造平滑的音色空间，提升对未见音色的泛化能力。

## 实验结果
- 在音色转移任务中，EG-VAE在Mel谱距离上比最强任务专用基线（One-to-many with EGTR enhancement）降低44%（0.86 vs 1.53，seen tones）。
- 在音色去除任务中，EG-VAE优于最佳EGTR模型（Distortion Recovery），Mel距离为1.10 vs 1.21（seen tones），在unseen tones上持平。
- 消融研究验证了各解耦机制和第二阶段设计的贡献，主客观评估均表明EG-VAE优于任务专用基线。

## 一句话评价
EG-VAE首次实现电吉他音色转移与去除的统一建模，通过音色掩蔽和两阶段训练有效解决了表征泄漏与泛化问题，是吉他音色建模领域的重要进展。

---

## 2. AffectDF: The Most Comprehensive Benchmark for Speech Deepfake Detection against Emotionally Expressive Attacks

**作者**: Aurosweta Mahapatra, Xiutian Zhao, Shreeram Suresh Chandra, Zihan Zhang, Zongyang Du, Ismail Rasim Ulgen, Kong Aik Lee, Nicholas Andrews, Carlos Busso, Berrak Sisman
**链接**: [2608.05507](https://arxiv.org/abs/2608.05507)
**分类**: Speech Deepfake Detection | **关键词**: Speech Deepfake Detection, Emotionally Expressive Attacks, Benchmark, Large Audio-Language Models, Text-to-Speech, Voice Conversion, Emotional Speech, Robustness, Cross-Domain Generalization

### 核心痛点
现有语音深度伪造检测（SDD）系统在常规基准上表现优异，但面临两个关键缺口：1) 数据集对情感表达性攻击覆盖不足，尤其是缺乏大规模、多样化的情感伪造数据；2) 对最新的大音频语言模型（LALM）攻击未纳入评估。现有情感伪造数据集（如EmoFake、EmoSpoof-TTS）规模小、攻击类型单一（仅VC或TTS），且主要基于ESD acted speech，缺乏自发性情感语音覆盖。

### 方法创新
提出**AffectDF**，号称最全面的情感表达语音深度伪造检测基准：
- 包含约260小时语音，21种攻击，覆盖5种情感状态（neutral、happiness、anger、sadness、surprise）。
- 攻击类型全面：TTS、VC、EVC（情感VC）、以及LALM-based EVC，同时涵盖acted（ESD）与spontaneous（MSP-Podcast）情感语音。
- 数据划分采用不重叠说话人和攻击系统，支持跨说话人和跨攻击泛化评估。
- 首次系统性地在情感表达攻击下评估SDD鲁棒性、跨域泛化、以及情感状态/攻击类型/acted vs spontaneous条件的影响。

### 实验结果
- 在AffectDF上评估多个SOTA SDD系统（RawNet2、AASIST、XLSR-SLS、XLSR-Mamba、ProSDD等）以及LALM-based检测器（Qwen2.5-Omni、Qwen3.0-Omni、Voxtral）在inference-only和supervised fine-tuning下的性能。
- 关键发现：基于常规基准训练的模型在AffectDF上严重退化，部分接近随机；大规模情感训练并未持续提升跨域鲁棒性；性能在不同情感状态、攻击族、acted vs spontaneous条件下差异显著。
- 表明现有SDD系统未能学到在情感和韵律变化下具有泛化能力的伪造表征。

### 一句话评价
AffectDF是首个系统评估情感表达攻击下语音深度伪造检测的全面基准，暴露了现有SDD系统在情感和韵律多样性下的根本缺陷。

---

## 3. Rethinking Automatic Music Mixing as Sequential Stem Blending

**作者**: Yen-Tung Yeh, Chung-Jui Chan, Yun-Ning (Amy)Hung, Yi-Hsuan Yang
**链接**: [2608.05506](https://arxiv.org/abs/2608.05506)
**分类**: Automatic Music Mixing / Audio Processing | **关键词**: automatic music mixing, stem blending, flow matching, latent diffusion, degradation-based data synthesis

## Core Pain Points
- Existing automatic music mixing (AMM) systems rely on **parallelized architectures** that process all input stems simultaneously in a single pass, making them inflexible (fixed number of stems/instrument types) and constrained by predefined effects topologies.
- Current datasets are not directly applicable for stem blending: multitrack mixing datasets focus on full mixture reconstruction, while source separation datasets provide no mixing processing supervision.
- Audio effects are traditionally modeled in the audio domain (DSP or waveform neural networks), requiring a fixed effects chain that limits expressive power.

## Method Innovation
- Proposes a **paradigm shift** from single-pass mixing to **sequential stem blending**, where each stem is blended into a growing submix one at a time, mimicking human mix engineers.
- Introduces a **latent flow matching model** (using rectified flow) that learns the stem blending transformation in a latent space, conditioned on the submix context, allowing arbitrary mixing transformations without predefined effects.
- Develops a **degradation-based data synthesis** strategy to construct paired training data from existing multitrack/source separation datasets, simulating realistic mixing scenarios (spectral degradations, reverberation).
- Supports **arbitrary number of input stems** and enables interactive workflows (e.g., blending a stem into an existing user-provided submix).
- Investigates stem ordering strategies (random vs. domain-knowledge-based) and shows ordering influences the mixing style.

## Experimental Results
- Evaluated on both stem blending and AMM benchmarks using objective metrics and subjective listening tests.
- Demonstrates effectiveness of the proposed approach and generalizes to the full AMM task.
- Reveals that stem ordering affects the resulting mixing style, confirming the context-dependent nature of sequential blending.

## One-Sentence Evaluation
The paper presents a novel and principled sequential formulation for automatic music mixing, achieving flexible and expressive mixing through latent flow matching and degradation-based data synthesis.

---

## 4. Diff2Mix: Controllable Music Mixing via Diffusion Models and Differentiable Audio Effects

**作者**: Yisu Zong, Jinjie Shi, Joshua Reiss
**链接**: [2608.05442](https://arxiv.org/abs/2608.05442)
**分类**: Automatic Music Mixing | **关键词**: Diff2Mix, Diffusion Model, Automatic Mixing, Differentiable Audio Effects, Style Control

## 核心痛点
现有自动混音方法要么是黑盒直接预测音频，要么是参数估计但固定效果链，且缺乏对制作风格的控制。大部分方法将自动混音和风格控制分离，难以在保持高质量混音的同时进行灵活的风格编辑。

## 方法创新
提出Diff2Mix，一个基于扩散模型和可微混音台的生成式自动混音系统。该系统提供两级用户控制：(1) 参考音频控制整体制作风格；(2) 可微混音台提供显式音频效果参数，实现可解释性和细粒度优化。核心组件包括：条件音频效果嵌入扩散模型（基于MEGAMI和EDM，采用分类器自由引导），以及音频效果参数解码器（直接参数估计或参数分布建模）。

## 实验结果
通过客观和主观评估，验证了该系统在混音质量和风格控制方面的竞争力。

## 一句话评价
Diff2Mix将扩散模型与可微音频效果相结合，首次实现了在同一系统中同时具备高质量自动混音和显式风格控制的能力。

---

## 5. Diff-Symbo: Text-Controlled Long-Duration Symbolic Music Generation Using Autoregressive Latent Diffusion Model

**作者**: Zhiwei Lin, Jun Chen, Boshi Tang, Weihao Wu, Yang Jing, Yaolong Ju, Fan Fan, Zhiyong Wu
**链接**: [2608.05222](https://arxiv.org/abs/2608.05222)
**分类**: Text-to-Symbolic Music Generation | **关键词**: Latent Diffusion Model, Symbolic Music Generation, Text-to-Music, Autoregressive Generation, Music Information Encoder

# Diff-Symbo 论文总结

## 核心痛点
- 文本控制的符号音乐生成在质量、多样性、可控性和时长方面存在不足。
- 现有方法中，自回归Transformer模型（如MuseCoco、MMT）可生成长音乐但质量和多样性欠佳；扩散模型（如Polyffusion）质量高但只能生成固定时长，缺乏灵活性。
- 缺乏文本-符号音乐配对数据集。

## 方法创新
- **Diff-Symbo**：将潜在扩散模型（LDM）与自回归方式结合，实现高质量、多样化、长时长的符号音乐生成。
- **数据集构建**：利用GPT-4生成19,345个文本模板，覆盖所有音乐属性组合，构建大规模文本-符号音乐数据集。
- **音乐信息编码器（MI-Encoder）**：基于冻结BERT和可学习查询，通过音乐属性分类任务提取有效控制表示，降低训练开销。
- **自回归生成**：引入音乐上下文模块，通过微调LDM实现分段生成，保证长时长音乐在风格、情绪和配器上的连贯性。

## 实验结果
- 与基线GPT-4、MuseCoco、MMT相比，Diff-Symbo在文本可控性、生成时长和音乐质量上均有显著提升。
- 能够生成数分钟长度的高质量、多样化符号音乐，且与文本描述精确匹配。

## 一句话评价
Diff-Symbo首次将LDM与自回归方法结合，有效解决了文本控制符号音乐生成中质量、多样性与时长之间的权衡问题。

---

