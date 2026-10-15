# Arxiv Daily Deep Report - 2026-10-15

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 45
---

## 1. Continued fractions and passive ladder networks for acoustic impedances: the baffled piston and the horn

**作者**: Ronald M. Aarts
**链接**: [2610.20371](https://arxiv.org/abs/2610.20371)
**分类**: Error | **关键词**: 

总结生成失败: 'NoneType' object is not subscriptable

---

## 2. CochlearMark: Audio Watermarking via Phase Locked Auditory Nerve Representations

**作者**: Qin Liu, Strahinja Nikolic, Milos Cernak
**链接**: [2610.20105](https://arxiv.org/abs/2610.20105)
**分类**: Error | **关键词**: 

总结生成失败: 'NoneType' object is not subscriptable

---

## 3. Quantizer Redundancy and Exact Index Recoding in a Frozen Neural Audio Codec

**作者**: Youssef Hemimy
**链接**: [2610.20471](https://arxiv.org/abs/2610.20471)
**分类**: Error | **关键词**: 

总结生成失败: 'NoneType' object is not subscriptable

---

## 4. vst-bench-ml: Auditable Dataset Generation for Audio Plugins

**作者**: Youssef Hemimy
**链接**: [2610.20465](https://arxiv.org/abs/2610.20465)
**分类**: Error | **关键词**: 

总结生成失败: 'NoneType' object is not subscriptable

---

## 5. Repairing Speech Access After Text Updates with Frozen Affine Fields

**作者**: Ming-Hao Hsu, Yuxiang Wang, Yingda Shen, Zhizheng Wu
**链接**: [2610.20253](https://arxiv.org/abs/2610.20253)
**分类**: Error | **关键词**: 

总结生成失败: 'NoneType' object is not subscriptable

---

## 6. Designing Textual Interfaces To Enhance Llm Reasoning On Audio-Visual Question Answering

**作者**: Yi Wang, Tianzi Wang, Tong Lei, Dahan Wang, Peter Bell
**链接**: [2610.20085](https://arxiv.org/abs/2610.20085)
**分类**: Error | **关键词**: 

总结生成失败: 'NoneType' object is not subscriptable

---

## 7. Few-Shot Adaptation for Anomalous Sound Detection at Low False-Positive Rate

**作者**: Simone Lugani, Christof Pichler, Hannes Wegleiter, Christoph Feilmayr, Rodolfo Zunino, Edoardo Ragusa
**链接**: [2610.19893](https://arxiv.org/abs/2610.19893)
**分类**: Anomalous Sound Detection | **关键词**: Anomalous Sound Detection, Few-Shot Learning, Predictive Maintenance

# 论文总结：Few-Shot Adaptation for Anomalous Sound Detection at Low False-Positive Rate

## 核心痛点
- 工业声学异常检测中，高假阳性率严重限制了系统的实际部署，尤其在大型设施中，少量误报即可影响系统可用性与接受度。
- 真实声学环境复杂：多台机器同时运行、背景噪声时变、额外干扰掩盖故障特征，使得可靠检测困难。
- 现有无监督异常声音检测（ASD）在低假阳性率（FPR）区域表现不佳，且故障发生后仅有少量异常样本可用，如何利用这些样本提升性能是迫切需求。

## 方法创新
- 提出两阶段ASD框架：
  1. **无监督预训练阶段**：采用卷积变分自编码器（CVAE）提取对数梅尔频谱图的潜在表示，并用高斯混合模型（GMM）对正常潜在分布建模；在GMM训练中引入协方差正则化，提升估计鲁棒性。
  2. **少样本自适应阶段**：首次故障后，利用单次故障的少量异常样本微调CVAE，GMM保持固定作为正常潜在分布的参考；设计复合损失函数，包含正常样本一致性项、异常样本分离项以及无监督重建正则项；通过时间偏移、裁剪、幅度缩放和频谱着色进行数据增强。
- 异常分数定义为GMM下潜在表示的负对数似然，分数越高越异常。

## 实验结果
- 在真实运行的高炉原料场采集的声学数据上进行评估，环境声压级约95 dB，包含13台振动筛及多种干扰。
- 少样本自适应将AUPR从23.0提升至64.0，低FPR区域的pAUROC从39.6提升至72.8，显著改善了低误报率下的检测能力。
- 协方差正则化同时提升了无监督模型的预测精度和训练稳定性。
- 与无监督基线（UNS）及带正则化的无监督模型（UNS R）相比，少样本自适应（FS）在AUPR和低FPR检测上均有大幅提升。

## 一句话评价
该论文提出了一种面向真实工业场景低假阳性率需求的实用两阶段少样本自适应ASD方法，并通过现场数据验证了其有效性。

---

## 8. Learning Visual Speech Representations via Cross-Modal Distillation and Joint Face-Lip Modeling

**作者**: Jing-Xuan Zhang, Genshun Wan, Jianqing Gao, Jia Pan, Yumei Zhang, Lichen Zhang
**链接**: [2610.19559](https://arxiv.org/abs/2610.19559)
**分类**: Visual Speech Recognition / Lipreading | **关键词**: Visual Speech Recognition, Lipreading, Cross-Modal Distillation, Audio-Visual Self-Supervised Learning, Face-Lip Joint Modeling, Whisper, Modality Dropout

# FLARE: 通过跨模态蒸馏与联合人脸-唇部建模学习视觉语音表征

## 核心痛点
- 唇读/视觉语音识别（VSR）中，视觉语音线索本身存在"视位-音素"映射的固有歧义，且对头部姿态和视频分辨率高度敏感。
- 现有音视频自监督学习（AV-SSL）方法大多从头联合学习音频、视觉与音视频表征，未能直接回答"如何组织监督信号才能最有效增强视觉表征"这一问题。
- 多数方法仅使用裁剪后的唇部 ROI，在头部姿态变化大、低分辨率或裁剪不完美时不可靠；已有全脸输入研究多停留在决策级融合，人脸与唇部线索的互补性尚未被充分挖掘。

## 方法创新
- 提出 FLARE 框架，用于鲁棒的视觉语音表征学习，核心由跨模态蒸馏和联合人脸-唇部建模组成。
- **跨模态蒸馏**：采用语义丰富的 Whisper 作为音频教师模型，通过随机投影量化器（random-projection quantizer）将教师表征转化为离散蒸馏目标，再以掩码预测目标进行预训练。
- **双流视觉建模**：唇部 ROI 流捕捉细粒度发音动作，全脸流编码更广的面部动态；两路经专用 ConvNeXt 风格前端后，通过通道拼接与 dropout 正则化融合。
- **模态 dropout**：预训练时引入辅助音频以促进跨模态对齐，并对音频/视觉以及人脸/唇部模态施加 dropout，鼓励学习鲁棒的纯视觉表征；在仅有唇部 ROI 的场景下，可通过将对应特征置零自然处理缺失人脸输入。
- **增强上下文编码器**：以改进的 Conformer 作为上下文编码器，引入 RoPE、GQA、SwiGLU 和 RMSNorm，提升局部与长时程时序建模能力。
- **下游适配**：FLARE 可作为视觉编码器，搭配轻量 Transformer 解码器以公平对比基线，或搭配 LLM 解码器（Adaptor + LoRA）探索可扩展性。

## 实验结果
- 在 LRS2、LRS3 以及域外 WildVSR 基准上评估，最佳模型词错误率（WER）分别为 11.7%、13.2% 和 34.3%。
- 渐进式设计研究验证了各主要组件的贡献。
- 进一步分析表明，联合人脸-唇部建模在视频分辨率退化及大头部姿态变化条件下提升了鲁棒性，并产生更具音素判别性的视觉表征。
- 代码与预训练模型已开源：https://github.com/jxzhanggg/FLARE。

## 一句话评价
FLARE 通过 Whisper 离散蒸馏与显式的人脸-唇部双流联合建模，在多个唇读基准上取得强性能，并证明了全脸线索在退化视觉条件下的互补价值，是 AV-SSL 视觉语音表征学习方向一项务实且有效的推进。

---

## 9. Revise-TTS: A Non-Masking Refinement Framework for Masked Diffusion Models in Text-to-Speech

**作者**: Wanli Sun, Dan Su, Anton Ragni
**链接**: [2610.19499](https://arxiv.org/abs/2610.19499)
**分类**: Zero-Shot Text-to-Speech | **关键词**: Text-to-Speech, Masked Diffusion Models, Zero-Shot Speech Synthesis, Hierarchical Binary Quantization, Generative Refinement Networks, Self-Correction

# Revise-TTS 论文总结

## 核心痛点
- **MDM-based TTS 的不可修正预测**：掩码扩散模型（MDM）通过加噪把干净语音 token 映射为掩码图，并学习反向去噪恢复 token。与自回归模型不同，MDM 在中间步骤会直接提交高置信度预测，后续推理步骤不能修改已提交 token。因此预测错误会累积、传播，降低合成语音质量。
- **两阶段 TTS 难以定位错误来源**：传统的 text-to-semantic 与 semantic-to-acoustic 两阶段系统中，生成错误来自哪个模块难以判断。
- **离散 token 量化瓶颈**：FSQ 对每个 latent 维度独立量化为固定标量层级，表示是扁平的；提高精度需要更多维度。大码本可保留更细声学细节、减少量化误差，但扩大 token 预测空间并增加训练难度；小码本易优化，却可能丢失语言和说话人信息。
- **TTS 中缺少纠错式生成研究**：视觉合成和文本生成已有 error revision 方法，但在 TTS，特别是 MDM-based TTS 中尚未充分探索。

## 方法创新
### 1. 总体框架 Revise-TTS
- 一个单阶段框架，将 **HBQ（Hierarchical Binary Quantization，分层二值量化）** 和 **GRN（Generative Refinement Networks，生成式精炼网络）** 用于零样本语音生成。
- 首先用 HBQ 替代 FSQ，为语音 token 引入可扩展的二值表示，并具有显式的 coarse-to-fine 结构。
- 其次训练 GRN 从“真实 token + 随机 token”的混合中重建 token 序列。推理时进行迭代精炼，通过随机丢弃一小部分先前预测 token 并重新预测，实现自纠正。
- 该框架可扩展到任何 MDM-based TTS 任务，作为替代的训练和推理方法。

### 2. 背景：MDM 的问题
- MDM 的 corruption 过程把干净 token map Y0 映射为噪声水平 t 下的掩码图 Yt；反向去噪时，模型按条件（文本 x、可选语音提示 YP、受损 token map Yt）预测每个掩码位置最可能的干净 token。
- 每个去噪步骤只把最高置信度预测提交到 Yt，并用于下一次迭代；已提交 token 不再改变。因此错误提交的 token 无法被修正，并影响后续预测。

### 3. HBQ：分层二值量化
- HBQ 作用于音频 tokenizer 中声学编码器与语义编码器融合后的表示 H（T×C），先做逐元素归一化 tanh(H)。
- 对每个标量 z，HBQ 进行 M 轮连续二值精炼：第 m 轮根据决策中心 c_m 产生二值标签 b_m，c_1=0，c_m 由前 m-1 个 bit 决定，b_m = 0 若 z <= c_m，否则为 1。
- 经过 M 轮后，每个标量由 M 个 bit 表示；例如 z=-0.113 编码为 011，对应离散索引 3 和量化值 -0.125。每轮把当前区间对半，最终最大量化误差为 2^(-M)。
- 两种紧凑表示：Y_ind ∈ {0,...,2^M -1}^(T×C) 和 Y_bit ∈ {0,1}^(T×C×M)。二者信息容量相同（每帧 C×M bits），但 Y_ind 需要 C 个 2^M 类分类，Y_bit 只需 C×M 个二分类。
- HBQ 与 FSQ 都是 lookup-free、无需显式 VQ 目标（如 commitment loss）的量化方法。区别是 HBQ 具有 coarse-to-fine 排序，FSQ 使用固定标量层级；HBQ 输出可直接 bitwise 预测，也可打包成整数索引。

### 4. GRN：面向 TTS 的生成式精炼
- 在 MDM 解码中引入重叠解码，遵循视觉合成中的 GRN 思路：保留正确 token，并在后续迭代替换错误 token。
- 两种模式：GRN_ind 和 GRN_bit，分别对应整数索引空间和展平 bit token 空间，共享训练与采样流程。
- **训练**：每次迭代独立采样保留率 l ~ U(0,1)；按 l 采样二值选择图 S；构造受损输入 F = S ⊙ Y0 + (1-S) ⊙ Y_rand。模型接收文本 x、语音提示 YP 等条件，用交叉熵损失重建全部目标声学 token：L_GRN = -1/(TQ) Σ log pθ(y0 | F, x, YP)。该 one-step 目标让模型学会从部分损坏输入重建完整 token map，替换损坏 token、保留正确 token。推理时保留率采用 cosine schedule，无需单独策略网络选择 token。
- **采样**：从随机 token map F0=Y_rand 开始；第 k 步由 F_k 预测 Ŷ_{k+1}；用保留率 l_{k+1} 采样 S_{k+1}；构造 F_{k+1}=S_{k+1} ⊙ Ŷ_{k+1} + (1-S_{k+1}) ⊙ Y_rand；l_{k+1}=ρ[1-cos(π/2 τ_{k+1})]，其中 ρ=0.999，τ_{k+1}=min((k+1)/(K-1),1)。未被选中的预测被随机 token 替换，并在下一步重新预测，从而允许早期错误被纠正。K 步后返回最终预测 Ŷ_K。

## 实验结果
- 摘要和实验部分说明：HBQ 使 Revise-TTS 在零样本语音合成上取得有竞争力的性能；消融实验进一步验证 HBQ 配置的有效性；框架可扩展到任意 MDM-based TTS。
- 实验设置（片段可见部分）：消融实验在 LibriTTS-R（585 小时英语，24 kHz）和 WenetSpeech4TTS premium 子集（945 小时普通话，16 kHz）上训练；主模型在 Emilia 的英语和普通话子集上训练，分别约 46.8k 和 49.9k 小时。
- 对比重点：FSQ 与 HBQ 在不同 C 和 M 组合下的配置；GRN_ind 与 GRN_bit 两种变体；此外涉及与 MDM-based TTS 纠错相关的基线或思路。
- 由于提供的论文片段在实验部分被截断，具体客观指标（如 WER、SIM、MOS 等）和数值结果未在片段中给出，需查看原文完整实验表。

## 一句话评价
Revise-TTS 把“非掩码式”可重叠生成精炼 GRN 与 coarse-to-fine 的 HBQ 结合，直击 MDM-based TTS 中 token 提交后不可修正导致误差累积的核心缺陷，构建了首个面向 MDM-TTS 的纠错框架；思路具有通用性和可扩展性，但最终效果仍需结合完整实验数值判断。

---

## 10. What Does LALM Post-training Learn? Rethinking Audio Understanding and Reasoning Capabilities

**作者**: Hua-Hsuan Chen, Xuanjun Chen, Wei-Chung Lu, Chih-Kai Yang, Yu-Xiang Lin, Sung-Feng Huang, Haibin Wu, Hung-yi Lee
**链接**: [2610.19476](https://arxiv.org/abs/2610.19476)
**分类**: Large Audio-Language Models (LALMs) | **关键词**: Large Audio-Language Models, Post-training, Audio Understanding, Audio Reasoning, Controlled Evaluation, Multiple-choice Question Format, Modality Shortcut

## 核心痛点
现有大型音频语言模型（LALM）在MMAU、MMAR等音频理解与推理基准上经过SFT、RFT、GRPO、VCRL等后训练后性能显著提升，但这种提升可能并非来自真正的音频理解与推理能力，而是模型对特定题目格式（尤其是多选题）和文本线索的适应。已有研究发现，即使没有音频或输入静音，模型也能获得部分增益，因此核心问题是：LALM后训练究竟学到了音频感知/推理，还是只学会了利用文本捷径答题？

## 方法创新
论文提出受控评测协议来解耦音频理解提升与题目格式适应，主要包含两个维度：
1. **音频 vs 静音评测**：对基座模型和后训练模型分别在真实音频与等长静音输入下评测，定义Audio Gain（ΔAcc_a = Acc_a^post - Acc_a^base）和Silence Gain（ΔAcc_s = Acc_s^post - Acc_s^base）。理想后训练应表现为ΔAcc_a大而ΔAcc_s接近0；若ΔAcc_s同样很大，说明提升不依赖真实音频。
2. **多选题 vs 开放式评测**：保留原始多选题格式，或去掉选项进行开放式生成，并用LLM judge判断语义等价，以检验性能提升是否依赖文本选项/答案模式。
实验统一训练预算、奖励函数（仅验证最终答案是否匹配金标选项）和训练配方（200步LoRA、3个随机种子），避免方法间配置差异干扰结论。

## 实验设置
- **训练数据**：来自Audio-Cogito的12,267条多选题音频QA，覆盖7,129个音频片段（17.4小时），包含AudioSet（声音）、Medley-solos-DB（音乐）、DailyTalk（语音）三个公开语料；划分为10,446条训练样本和1,821条域内评测样本，并验证训练音频未泄漏到评测集。
- **后训练方法**：SFT、RFT、GRPO、VCRL。
- **基座模型**：Qwen2.5-Omni-3B、Qwen2-Audio-7B-Instruct。
- **评测基准**：MMAU test-mini（1,000条）、MMAR（1,000条）；细粒度能力按MMAU category和MMAR layers划分；开放式评测使用Qwen3.6-27B作为LLM judge。

## 主要结果
1. **音频与静音增益高度相关，后训练并未教会模型听音频**：GRPO在Qwen2-Audio-7B-Instruct上使MMAU提升+14.8，但在静音下仍保留+11.2；在MMAR上+7.2，静音下+4.9。反之，若Silence Gain接近0（如RFT在Qwen2.5-Omni-3B上），Audio Gain也仅约+0.9，说明增益往往来自与音频无关的文本/猜测策略。
2. **开源模型同样存在该现象**：R1-AQA和Audio-Reasoner在MMAU上Audio Gain分别达+23.4和+20.5，但Silence Gain仍高达+17.2和+18.4。AudioMCQ虽专门用高音频依赖样本训练，MMAU上Audio Gain为+5.0，而Silence Gain为+6.4，即无真实音频时提升反而更高。
3. **增益依赖文本题目格式**：在开放式评测中，去掉选项后模型性能严重下降，后训练带来的报告增益几乎消失，表明大部分提升来自对多选题格式和文本线索的利用。
4. **细粒度音频能力提升有限**：按MMAU的Reasoning、Info Extraction、Signal Perception和MMAR的Semantic、Cultural等能力分析，静音增益在推理/信息提取等文本相关能力上较明显，而在信号感知等真正依赖音频的能力上增益微小甚至为负，进一步质疑模型实际的音频理解与推理能力。

## 结论与一句话评价
论文通过音频/静音与多选题/开放式的受控对照，系统揭示LALM后训练报告的大部分性能提升来自任务特定文本线索和答案模式，而非可泛化的音频理解与推理；一句话评价：该工作对当前LALM音频推理评测与训练奖励设计提出了重要警示——若不控制文本捷径，后训练可能只是在教模型更会做题而非更会听音频。

---

## 11. Point-and-Play: Instrument Timbre Cloning from Music Mixtures

**作者**: Baotong Tian, Zhiyao Duan
**链接**: [2610.19445](https://arxiv.org/abs/2610.19445)
**分类**: Instrument Timbre Cloning | **关键词**: Instrument Timbre Cloning, Polyphonic Music, Cue-Gated Statistics Pooling, CLAP, Flow Matching, Neural Instrument Synthesis

# Point-and-Play: Instrument Timbre Cloning from Music Mixtures

## 核心痛点
- 现有神经乐器合成器能从独奏乐器克隆音色，但目标乐器常嵌入在完整制作的多乐器录音中，现有方法难以直接处理。
- 先做源分离再克隆会面临分离伪影传播，且波形重建并非本任务必需，可能引入不必要偏差。
- 需要从复音混音中直接提取被提示音源的可复用音色，同时丢弃竞争源和音高、力度等内容信息。

## 任务定义与贡献
- 形式化新任务 **instrument cloning from music mixtures**：给定多乐器复音混音，通过音频示例或文本提示（乐器名）指定目标乐器，克隆其音色并用于合成未出现在混音中的新音高和力度。
- 区别于从孤立乐器录音克隆音色，也区别于 text-to-instrument generation：文本指定想生成的乐器，而非从混音中识别并恢复某源音色。
- 贡献：1）提出新任务并建立评估协议；2）提出 Point-and-Play，首个从复音混音克隆被提示源并合成新音高/力度的系统；3）实验表明音色保真度接近干净独奏参考，并优于 separate-then-clone 基线。

## 方法创新
- **直接混音编码**：不先分离目标源，直接从混音中推断音色。
- **Cue-Gated Statistics Pooling (CGSP)**：用 cue 选择性地聚合 adapted CLAP 混音 token，生成 timbre code z。
- 双分支：可训练混音分支 = CLAP 音频编码器 + LoRA 微调，输出全局码 g 和 token 序列 H；冻结 cue 分支 = CLAP 音频/文本编码器，输出 cue embedding q。
- CGSP 三阶段：1）cue–token gating，用独立 sigmoid 门控计算每个 token 权重；2）加权统计聚合，计算加权均值 μ 和标准差 σ_h；3）残差融合，MLP Rθ 将 [μ;σ_h] 映射为混音条件残差，加到归一化 cue embedding 上，再归一化得到 z。最终层零初始化，使 z 初始接近 cue 先验，逐渐学习混音证据。
- **训练目标**：四个互补损失：L_inv（配对混音全局嵌入对齐，内容不变性）、L_aalgn（音频 cue 提取的 z_a 对齐孤立目标 CLAP 教师嵌入 t）、L_talgn（文本 cue 提取的 z_t 对齐 t）、L_asel（用错误类别音频 cue 提取的 z̄_a 推离 t，增强 cue 选择性）。总损失 L_E = λ_inv L_inv + λ_a L_aalgn + λ_t L_talgn + λ_s L_asel。音频 cue 来自同类别不同乐器，防止直接复制 cue 音色；文本 cue 未使用 L_asel。
- **条件音符合成器**：冻结提取器，训练基于 FlowSynth 的 latent note synthesizer。条件 c = W_z z + E_p(p) + E_v(v)，其中 z 为 512 维 timbre code，p 为音高，v 为力度；通过 AdaLN 调制每个 DiT block。使用 Conditional Flow-Matching 损失训练 Transformer F_φ。推理时从高斯噪声积分生成 latent，用冻结 VAE decoder 解码，生成多个候选并选择与 z 的 CLAP 余弦相似度最高者。

## 实验结果
- 训练数据来自 NSynth、NLakh、Slakh、MoisesDB 四个语料，采样权重 0.30/0.30/0.10/0.30；混音片段长度 4 秒。NSynth/NLakh 随机选 4/953 乐器并独立采样两条 4 秒片段形成配对混音；Slakh/MoisesDB 从同一歌曲采样两个 4 秒窗口并保留所有 stem。
- 评估使用 27 个 NSynth 留出乐器；Figure 3 额外使用排除出提取器训练的 MoisesDB 评估子集。
- 实现：混音编码器初始化自 LAION-CLAP 音乐域检查点的 HTSAT-base audio tower，用 rank-8 LoRA（α=16）微调 qkv、fc1、fc2 投影；仅训练 LoRA 参数和 CGSP head。冻结 cue/teacher 编码器及候选选择嵌入使用同一音乐专用检查点。文本 cue 为粗粒度乐器类别名（如 “guitar”）。提取器训练 18k 步，AdamW，batch size 16，InfoNCE 温度 0.1，学习率 500 步 warmup 到 3e-4，余弦衰减到 3e-5，单张 A100 约 3 小时。损失权重 λ_inv=λ_a=λ_t=1，λ_s=0.25。合成器为 24 层 DiT，hidden width 1024，16 个 attention heads，AdaLN 条件。
- 结果：Point-and-Play 在音色保真度和合成质量上优于 separate-then-clone 基线，并达到与从干净独奏乐器克隆相当的性能。消融见 Table 2（四个训练目标）。

## 一句话评价
Point-and-Play 通过 cue-gated 统计池化直接从复音混音中提取被提示乐器音色，绕开源分离，实现了可播放的乐器克隆，并在音色保真度上媲美干净独奏参考。

---

## 12. PhonoVoxtLM: Exploring Single-Codebook Phonological Tokens for Speech Understanding and Generation

**作者**: Mingrui Liang, Kentaro Onda, Shinji Watanabe
**链接**: [2610.18469](https://arxiv.org/abs/2610.18469)
**分类**: Unified Speech Language Modeling | **关键词**: single-codebook speech tokens, phonological tokens, unified speech language model, speech understanding and generation, spoken question answering, speech tokenization

# PhonoVoxtLM 论文总结

## 核心痛点
- 统一语音理解与生成需要离散语音表示同时承载语言内容与韵律/声学信息，但现有 token 往往偏向一端：声学 token 利于合成但不利于理解，内容导向 token 利于识别但生成质量受限。
- 已有系统常通过多码本、额外 token predictor、或组合多种 token 类型来弥补单一表示的不足，增加了建模与训练复杂度。
- 缺少对“同一表示同时作为输入与生成目标”在理解与生成两类能力上的系统评估，尤其在识别与合成之间的权衡尚不清晰。

## 方法创新
- 提出 PhonoVoxtLM，基于 VoxtLM 的统一自回归框架，用音系 token（phonological tokens）替代 HuBERT units，作为共享的语音输入与生成目标。
- 采用预训练 Phonological Tokenizer（Onda et al., 2026）：通过可微 k-means 联合 ASR 与语音重合成目标，保留语言内容与韵律信息；使用 fine-tuned WavLM-large 编码器第 21 层特征，K=2,000 聚类中心，编码器与聚类中心在 LM 训练和 SQA 适配中均冻结。
- 单码本设计：语音 unit 直接作为输入和输出目标，不引入额外语音 token 预测模块或多 token 流。
- 语音 unit 索引映射到 CJK 统一表意文字区块 Unicode 0x4E00+di，使语音符号可与文本一起被 SentencePiece Unigram 建模，形成联合语音-文本子词词表。
- 使用 OPT 初始化的 decoder-only Transformer 作为共享语言模型，通过控制 token（<sS>、<sT>、<gS>、<gT>）统一 TextLM、SpeechLM、ASR、TTS 四类任务；语音输出经 SentencePiece 解码、符号到 unit 映射后，由 unit-conditioned HiFi-GAN 合成波形。
- 进一步扩展到 spoken question answering（SQA），形式化为 pθ(A|S,Q)，在 LibriSQA Parts I/II 上以答案生成目标微调，并混入 ASR、TTS、TextLM、SpeechLM 的 replay 样本，仅更新共享语言模型，保持 tokenizer 与 SentencePiece 固定。

## 实验结果
- 在不同训练数据规模下，PhonoVoxtLM 相比 1K 和 2K HuBERT k-means 基线，在语音理解与生成任务上均取得提升。
- 与 WavLM-large k-means token 相比存在明显权衡：音系 token 改善合成，而 WavLM 基线在识别和语音判别方面更好。
- 在 SQA 上，经 replay 适配后的 PhonoVoxtLM 优于同样适配的 HuBERT 基线，同时保留原始语音任务上的优势。
- 实验还比较了 codebook 大小、语音编码器选择与训练数据规模，并在 ESPnet recipes 上实现训练与推理流程，强调共享表示应同时在理解与生成能力上评估。

## 一句话评价
PhonoVoxtLM 证明面向内容与韵律的单码本音系 token 可作为统一多任务语音建模的实用共享表示，在理解与生成上优于 HuBERT 基线，但仍需面对相对 WavLM 的识别-合成权衡。

---

## 13. Self-Supervised Source-Filter Model of Speech Production

**作者**: Nani Meka (1), Raghavan Ramesh (1), Sri Rama Murty Kodukula (1) ((1) Speech Information Processing Lab, Indian Institute of Technology Hyderabad)
**链接**: [2610.18120](https://arxiv.org/abs/2610.18120)
**分类**: Speech Production Modeling | **关键词**: Self-Supervised Learning, Source-Filter Model, Formant Estimation, Fundamental Frequency Estimation, Speech Production, Interpretability

## 核心痛点
- 现有深度学习语音模型大多依赖与发音/发声无物理对应的隐特征，缺少可解释的源-滤波器（source-filter）描述。
- 语音产生中，源（F0、清浊、非周期性）与滤波器（共振峰、反共振）共同变化且相互纠缠；在浊音中滤波器包络只在谐波频率处被观测，导致二者估计误差互相传播。
- 共振峰估计更难：Praat/WaveSurfer 等全极点 LPC 方法无法表示鼻音/边音反共振，高 F0 时包络被单个谐波牵引，极点到共振峰的分配依赖启发式。
- 基频估计较成熟，但经典跟踪器存在八度错误、阈值依赖；监督网络依赖标注/合成数据；自监督方法存在偏移标定或合成覆盖问题。
- 无标注时逐频点谱重构损失存在系统性盲点：偏好宽而模糊的谱峰和噪声谱，导致 F0 梯度弱、非周期性被低估、共振峰过宽且峰谷过浅。

## 方法创新
- 提出 SoFilNet：一个自监督、可微的 Source-Filter Network，直接从原始波形估计语音产生参数；每个 10 ms 帧输出源参数 λg={F0, u, a1...a5} 与滤波器参数 λv（有序共振峰极点、塑造其余谱包络的附加极点、反共振零点）以及帧增益 γ。
- 可微合成器：将 λ 映射为帧谱，与观测谱比较并反向传播；共振峰身份由构造保证，无需跟踪或标注。
- 源模型：谐波+噪声混合。谐波梳由 F0 决定，噪声为每频点独立指数分布的白高斯，五个频带（0–1, 1–2, 2–4, 4–6, 6–8 kHz）的非周期性 a_b 线性插值成 a(ω)。源功率谱为 |G|^2 = u[(1-a)|Gh|^2 + a|Ga|^2] + (1-u)|Ga|^2。
- 滤波器模型：零极点级联的有理传递函数 V(z)，极点对产生共振峰，零点对产生反共振；极点带宽约 B_k = -(fs/π) ln r_k，半径越接近 1 共振越尖锐。
- 训练目标针对逐频点损失的盲点：F0/清浊用自相关伪标签，并随后用模型自身声道的逆滤波残差精炼；非周期性用频带周期能量比例代理；共振峰尖锐度用频带谱对比度训练。

## 实验结果
- 在 VTR-FORMANTS 上，估计共振峰取得所报告方法中最低平均误差，包括监督式跟踪器。
- 在未见过的 PTDB-TUG 语料上，F0 帧误差与最佳经典跟踪器相当，并低于所有学习式跟踪器。
- 参数符合语音产生理论：频带非周期性随频率上升，并按激励湍流程度对音素类别排序；鼻辅音上零点加深，较低零点随发音部位上升。

## 主要贡献
- 从原始波形估计的可微源-滤波器模型，源含频带非周期性，滤波器中共振峰按构造有序。
- 三个无标注训练目标：精炼自相关伪标签（F0/清浊）、频带周期比例损失（非周期性）、谱对比度损失（共振峰尖锐度）。
- 在共振峰与 F0 跟踪上达到强竞争力，且参数具有语音产生理论可解释性。

## 一句话评价
SoFilNet 用自监督可微合成把语音的源-滤波产生过程显式分解为可解释参数，在无标注条件下取得有竞争力的共振峰与 F0 跟踪性能，并展现出与语音产生理论一致的参数行为。

---

## 14. Modeling and Design of a Diaphragm-Integrated Photonic Waveguide Microphone

**作者**: Xiaoyu Niu, Yuqi Meng, Zihuan Liu, Ehsan Vatankhah, Neal Hall
**链接**: [2610.17745](https://arxiv.org/abs/2610.17745)
**分类**: Optical MEMS Microphone / Integrated Photonic Acoustic Sensing | **关键词**: Integrated photonic sensing, Diaphragm strain, Mach–Zehnder interferometry, Optical MEMS microphone, Acoustic sensitivity, Shot noise, Acoustic overload

# 论文总结：Modeling and Design of a Diaphragm-Integrated Photonic Waveguide Microphone

## 核心痛点
- 传统电容式/压电式微型麦克风受背板相关热机械噪声、背腔噪声、ASIC高输入阻抗噪声等限制，噪声预算决定动态范围与可用工作区间。
- 论文追问：去除电容式振膜接口与独立背板、改用集成光学读出后，在计入光学噪声与声学过载后，是否仍能带来有用的性能优势？
- 已有集成波导麦克风验证了光学传感可行性，但缺少将压力致振膜弯曲→波导伸长→光电流串联起来的解析模型，也缺少机械灵敏度与光学检测极限的分离评估。

## 方法创新
- 提出振膜集成 Mach–Zehnder 干涉仪（MZI）麦克风解析模型：参考臂置于支撑基底，传感臂置于振膜；振膜弯曲改变传感臂光程，干涉将相位变化转换为强度变化。
- 采用 MMI 分束/合束；可片上集成激光器与光电探测器，也可由外部光学组件询问传感芯片。
- 建立耦合机械-光学模型：压力→路径差→光电流。光学功率传递函数为 Eq.(1)，光电流为 Eq.(2)，光学灵敏度 S_op 为 Eq.(3)，散粒噪声极限最小可探测位移 MDD 为 Eq.(4)，本征光学动态范围 DR 为 Eq.(5)。
- 噪声预算保留两个主项：光学散粒噪声 i_shot 与背腔热机械噪声 i_BC，并按 1 Pa 输入计算 SNR，见 Eq.(6)-(7)；总电流灵敏度 S_T = S_op × S_m。
- 过载判据：10% 总谐波失真（THD），允许光程偏移限制在 65% λ/2。
- 评估两个工作区间：紧凑 MEMS 麦克风 1 mW 光输入，测量麦克风 100 mW 光输入；调制效率 ME 取 50% 或 100%，R_op=0.5 A/W，q=1.6×10^-19 C。与约 110 dB 动态范围、约 1 mW 功耗的 MEMS 基准进行比较。

## 实验结果/性能预测
- 紧凑情形：1 mm 直径、1 μm 厚、无应力硅振膜，100% 调制效率，预测信噪比 78 dB，声学过载压力 124 dB。
- 高功率情形：100 mW 光输入降低建模噪声底，并相对所选测量麦克风基准提高动态范围。
- 本征光学 DR 在 dB 域由 Eq.(5) 给出；线性域中随光输入功率的平方根增加。但作者强调，光学输入功率与完整麦克风功耗不能直接比较，单独的光学 DR 不证明 ME=100% 或 ME=50% 具有系统级优势。
- 历史对比：光学光栅麦克风封装 4.14 mm×4.15 mm×1.38 mm，报道噪声底 22.00 dBA，SNR 72 dB；该对比面向 2014 年可用麦克风，应视为历史基准。
- 作者明确：这些估计依赖有利假设，不构成已制备波导麦克风的实验验证；所提传感头的温度容忍度尚未验证，需通过测量检验预测性能。

## 一句话评价
- 该工作提供了振膜集成 MZI 波导麦克风的解析建模与压力参考噪声预算框架，清晰给出光学读出在紧凑/高功率场景下的性能上界与设计折衷，但结论仍属理论预测，尚需实验验证，且未证明其相对传统麦克风具有总体优势。

---

## 15. Co-Adaptive Entropy Modeling and Rate-Distortion-Optimal Bit Allocation for Perceptual Audio Coding

**作者**: Soohyun Kim, Jiwon Jeong, Marina Bosi
**链接**: [2610.17459](https://arxiv.org/abs/2610.17459)
**分类**: Perceptual Audio Coding | **关键词**: 感知音频编码, 率失真优化, 熵编码, 算术编码, 比特分配, 自适应熵模型, MUSHRA, 动态规划, 心理声学模型

# 论文总结：面向感知音频编码的协同自适应熵建模与率失真最优比特分配

## 核心痛点
传统感知音频编码通常将量化噪声掩蔽在心理声学阈值以下，并使用固定或局部可变的比特预算在频带间分配比特。其比特分配多依赖静态或经验率模型，例如基于固定 Huffman 表或简单“比特×谱线数”模型；而自适应熵编码（CABAC、USAC CAAC、G.719 等）虽然能根据已解码上下文在线自适应，但其自适应状态并未参与比特分配定价。已有工作如 Aggarwal 等的 AAC 网格搜索、Oger 等的广义高斯谱模型加自适应算术编码、AC-3 的混合后向/前向自适应分配，均未真正闭环连接“后向自适应熵模型”与“离散率失真最优比特分配”。关键痛点是：如果熵模型在线从已解码数据学习，比特分配阶段本可零边信息成本地感知每个候选量化选择的当前编码代价，但此前没有感知音频编码器做到这一点。

## 方法创新
1. **熵编码感知的比特分配**：每个频带的率失真前沿由两部分构成——测得量化失真（按掩蔽阈值加权，即线性尺度 NMR）与当前算术编码模型下的熵编码率估计（交叉熵估计）。率估计避免试编码，仅作为写入代价的代理，残差由 reservoir 吸收。
2. **精确与近似求解器**：采用网格动态规划（DP）在模型率估计下精确最小化每个块预算的总目标感知失真，不要求前沿凸性；同时对比 BFOS 风格边际分析求解器与拉格朗日求解器，揭示质量–复杂度权衡。DP 复杂度为 O(KB F̄) 时间、O(KB) 回溯内存。
3. **因果协同自适应**：编码器和解码器从已解码尾数累积共享的“比特精度×频带”直方图模型，并同步推进同一模型状态，不传输模型边信息。通过“编码器自适应但分配成本冻结”的控制实验，隔离分配反馈带来的增益。
4. **混合熵编码层**：尾数采用比特打包与算术编码混合，尺度因子以相邻频带差分静态模型编码；每个“精度×频带”使用最大似然双几何分布初始化，在线更新。低频带（0–34）因每带尾数少、8 比特头开销大，退化为比特打包；从第 35 带起启用混合选项。
5. **系统集成**：PCM 输入，16-bit 立体声 44.1 kHz，左右声道独立编码，无联合立体声工具。使用正弦窗 MDCT，N=1024 谱线（2048 样本块、50% 重叠），按 ERB 等宽分为 K=50 个尺度因子带。块浮点量化器使用 4-bit 尺度因子与每带尾数精度 b_k ∈ {0} ∪ {2,...,16}。侧链 FFT 心理声学模型给出每带 SMR_k；掩蔽曲线上升段 27 dB/Bark，下降段 27−0.367(L−40) dB/Bark。每块每声道编码器构建率失真前沿、求解分配、写入带内 AC/比特打包选择，随后编解码双方更新共享熵模型，未用比特进入 reservoir。

## 实验与结果
- 测试集：6 个标准片段，64 与 80 kbps/channel 下的客观失真与 CPU 时间；80 kbps/channel 进行 MUSHRA 听音测试。
- 严格每块速率下，熵编码感知比特分配相比同一求解器但无熵编码感知，降低总目标感知失真 15–24%。
- 协同自适应进一步降低 3–4%，在双簧管片段上最高可达 15%；这是仅后向自适应编码器单遍无法实现的增益。
- 无界 reservoir 时，增益缩小至 1–3% 与 0.3–0.5%；完整系统达到传统 water-filling 的 57–63%。
- MUSHRA 听音测试中，精确 DP 条件比 water-filling 高 22–25 分，协同自适应再提升 3.4 分。
- 无界 reservoir 下平均 payload 速率为 63.99 与 79.99 kbps/ch，所有流最终 reservoir 非负；文件头、32-bit 每声道块长字段、字节对齐与最终 flush 块额外增加约 1.7–1.8 kbps/ch。原型未限制瞬时速率，也评估了有界 reservoir 策略。

## 一句话评价
该论文首次将后向自适应熵模型与离散率失真最优比特分配闭环耦合，在零模型边信息下实现块级协同自适应，并通过精确 DP、近似求解器对比和主观听音验证，显著优于传统 water-filling 与无熵编码感知的分配方案。

---

## 16. Active noise cancellation extends the benefit of AI speech enhancement in real hearing-aid recordings

**作者**: Andrew T. Sabin, Linkai Li
**链接**: [2610.17287](https://arxiv.org/abs/2610.17287)
**分类**: Hearing Aid Speech Enhancement | **关键词**: Active Noise Cancellation, AI Speech Enhancement, Hearing Aids, Direct Path, SII-weighted SNR, Speech-in-Noise

# 论文总结：Active noise cancellation extends the benefit of AI speech enhancement in real hearing-aid recordings

## 核心痛点
- 助听器中的 SNR 提升算法只作用于放大路径，而未经处理的声音仍通过通气孔或耦合直接到达鼓膜（direct path），限制实际可实现的 SNR 增益。
- 低频通气最透明、处方增益通常最小，因此 direct path 造成的 SNR 天花板在低频最严重。
- ANC 在耳机中常见，但在助听器中罕见，其对噪声中言语理解的价值尚未确立。
- 前期仿真预测 ANC 衰减 direct path 可放大 SNR 增强处理的获益，但缺少真实硬件录音验证。

## 方法创新
- 在 KEMAR 上比较三种硬件条件：标准 RIC（Orka O1）、ANC-capable RIC（Orka O1 Pro）关闭 ANC、开启 ANC；每种硬件条件下 AI-SE 开或关，共 6 个助听条件。
- 所有条件按 Bisgaard N3 听力图和 NAL-NL2 经验用户目标验配，并以相同助听器信号处理套件运行，以隔离硬件、耦合与 ANC 状态影响。
- 使用 7 个高于 70 dB SPL 的 ARTE 真实声场景（咖啡厅、晚宴、街边阳台、火车站、美食广场等），共 42 条录音每个条件；双耳 44.1 kHz 记录，并配 open-ear 与干净语音参考。
- 用基于干净语音的二进制时频掩码估计录音中的语音与噪声频谱；以 STFT 2048 Hann 窗、512 hop 分析。
- 关键指标：每频带 SNR、Added SNR（相对 open ear）、AI-SE benefit（AI-SE on 减 off）、AI-SE benefit 低频边缘、ANSI S3.5-1997 SII 加权 Added SNR；REIG 与 REOIG 分别估计放大路径与直接路径。

## 实验结果
- REIG：三种硬件条件从低频近 0 dB 升至约 7 kHz 处 15–19 dB 峰值；ANC on 在约 550 Hz 以下出现负 REIG，说明 ANC 去除了部分 direct-path 声音。
- REOIG 与 direct path：Standard RIC 到约 2 kHz 仍近 0 dB；ANC RIC ANC off 在约 500 Hz 以上低于 0 dB，3.5 kHz 附近约 -27 dB；ANC on 在 100 Hz 为 -10 dB，200 Hz–1 kHz 为 -20 至 -28 dB。三种条件对 direct path 的隔离逐步增强。
- Added SNR：即使 AI-SE off，三条件在 1 kHz 以上均有提升（Standard 峰值约 1.8 dB，两个 ANC RIC 约 3.5 dB），归因于波束形成与传统降噪等。AI-SE on 后，Standard RIC 主要在 1 kHz 以上提升，4–5 kHz 峰值约 5.5 dB；ANC off 延伸至约 500 Hz，1.5 kHz 峰值约 7.5 dB；ANC on 正增益覆盖几乎全频段，峰值约 7.5 dB。
- AI-SE benefit：三条件在 4–6 kHz 均有约 4 dB 峰值；但获益低频边缘分别为 1500 Hz（Standard RIC）、600 Hz（ANC off）、130 Hz（ANC on）。这些边缘与 direct-path 衰减吻合。
- 按 ANSI 频带重要性加权，上述边缘及以上频带分别携带约 53%、84%、100% 的语音频谱重要性。
- 宽带汇总：AI-SE on 时，ANC RIC ANC on 相对 open ear 的 SII 加权 SNR 提升 5.1 dB；ANC off 为 3.3 dB；Standard RIC 为 1.6 dB。AI-SE off 时，开启 ANC 仅增加 0.2 dB。
- 结论：ANC 本身几乎不直接提升 SNR，但通过衰减 direct path，使放大路径中的 AI-SE 获益能在鼓膜处实现并扩展到更低频率，因此 ANC 是使能技术。

## 一句话评价
该研究用真实助听器录音验证了 ANC 的关键使能作用：它本身不改变 direct-path SNR，却能把 AI 语音增强的 SII 加权 SNR 获益从 1.6 dB 提升到 5.1 dB，并把有效获益频率下限从 1500 Hz 扩展到 130 Hz。

---

## 17. MSVAE: Rethinking Musical Semantics in Continuous Latent Spaces

**作者**: Guobin Ma, Yuepeng Jiang, Dake Guo, Huakang Chen, Yuan Zhou, Lingxin Xiong, Wenkai Cheng, Jingbin Hu, Hanke Xie, Chunbo Hao, Wenhao Li, Ziqian Ning, Jixun Yao, Jian Zhao, Zhonglin Jiang, Yong Chen, Lei Xie, Pengcheng Zhu
**链接**: [2610.17187](https://arxiv.org/abs/2610.17187)
**分类**: Music Generation (Lyrics-to-Song / Text-to-Music) | **关键词**: MSVAE, Music Semantic VAE, Continuous Latent Space, Lyrics-to-Song, Text-to-Music, Dual-Stream Alignment, Semantic-First Gated Residual Posterior

## 核心痛点
- 连续潜表征是近期基于扩散的歌词到歌曲（lyrics-to-song）和文本到音乐（text-to-music）系统的基础，但歌词条件与连续潜变量之间的对齐仍然困难。
- 现有系统多在生成器侧打补丁：句级时间戳、辅助对齐目标、后训练奖励、半自回归解码等；其预测的潜变量仍主要来自仅以波形重建为目标训练的 autoencoder。
- 纯重建训练保留声学细节，但不会保证旋律、和声、歌词相关语言信息在潜空间中显式且可预测地组织，导致下游生成器承担大量内容建模压力。
- 音乐语义包含两个互补流：作品级作曲内容（旋律/和声）与歌词级语言-人声内容；二者并非独立音频源，歌声旋律同时承载作曲与语音信息，因此需要在不相互干扰的前提下显式建模。

## 方法创新
- 提出 MSVAE（Music Semantic Variational Autoencoder）：将立体声音频编码为 25 Hz、64 维随机连续表示 z∈R^{T×64}。
- 分区双流语义对齐（Partitioned Dual-Stream Semantic Alignment）：把 z 沿通道分为两个 32 维子空间 z_comp 与 z_ling；分别用独立投影头对齐冻结的 SheetSage（旋律转写与和弦识别隐藏态，构成作曲参考）和 FireRedASR-AED-L（最终编码器隐藏态，构成语言-人声参考）。参考表示保持未投影，投影头仅在 VAE 训练时使用。对齐损失为特征轴上的 sigmoid-cosine 目标。分区设计限制两个对齐目标间干扰，鼓励互补特化。
- 语义优先门控残差后验（Semantic-First Gated Residual Posterior）：以冻结 MuQ 编码器第六层特征为语义基底，参数化对角高斯后验的均值与 log 方差；可训练声学残差编码器只通过由投影 MuQ 特征门控的有界残差修正引入重建相关声学信息，避免重构目标主导融合并削弱语义组织。
- 训练目标联合包含重建损失、对抗损失、KL 正则以及两个流特定对齐目标。

## 实验结果
- 摘要报告：MSVAE 取得有竞争力的立体声重构性能，在 MARBLE probing 上强于连续 autoencoder 基线，并改善下游 lyrics-to-song 与 text-to-music 生成。
- 显著优势：仅使用无时间信息的音素前缀、无歌词时间对齐时，MSVAE 取得最低 phoneme error rate；而所有基线表示需要句级对齐才能生成可懂人声。
- 论文还通过表 4 比较全维对齐与分区对齐设计。

## 一句话评价
MSVAE 从表示侧重新思考音乐语义，用双流分区对齐与语义优先门控残差后验把音乐语义显式嵌入连续 VAE 潜空间，从而缓解歌词-音频对齐难题并提升下游生成。

---

## 18. Spiking Neural Beamforming for Multichannel Speech Enhancement on the Edge

**作者**: Hanan Beit-On, Eli Shapira, Boaz Rafaely
**链接**: [2610.16430](https://arxiv.org/abs/2610.16430)
**分类**: Speech Enhancement | **关键词**: Spiking Neural Networks, Multichannel Speech Enhancement, Beamforming, Edge Computing, Neuromorphic Computing, Leaky Integrate-and-Fire

# 论文总结：Spiking Neural Beamforming for Multichannel Speech Enhancement on the Edge

## 核心痛点
- 单通道语音增强主要依赖谱时线索，在多说话人和混响场景下性能下降。
- 多通道神经波束成形虽能利用麦克风阵列空间信息，但计算和内存开销大，难以部署在功率和资源受限的边缘设备上。
- 现有基于 SNN 的语音增强方法大多局限于单通道处理，未利用空间多样性；部分方法混合 SNN 与 ANN，或使用高维脉冲表示而非顺序脉冲序列，导致参数量较大。

## 方法创新
- 提出全脉冲神经网络框架 FC-SNN，用于多通道语音增强。FC-SNN 由紧凑的全连接 ANN 基线（FC-ANN）通过将 ReLU 激活替换为 LIF 神经元转换而来，并加入脉冲编码与解码阶段。
- 采用顺序脉冲编码，比较两种方案：
  - 直接编码：每个输入特征在所有时间步保持恒定重复，第一层线性层仍为密集计算，仅下游 LIF 层脉冲驱动。
  - 速率编码：输入通过 Bernoulli 过程转换为随机脉冲序列，所有层（包括第一层）均为脉冲驱动，但需要更长的脉冲序列并引入量化噪声。
- LIF 神经元：膜电位 u[t] = beta * u[t-1] + I[t]，超过阈值 theta 时发放脉冲并复位；使用代理梯度学习，基于 snnTorch 实现。
- 脉冲解码：对最后一层脉冲在 N 个时间步上取平均，经 logit 函数映射为无界估计，形成复数掩码。
- 系统分析增强性能随模型大小和脉冲序列长度的缩放关系，并报告参数量、MACs 和 SynOps 等复杂度指标。

## 实验设置
- 数据集：WSJ0 语音语料；模拟半圆形 6 麦克风阵列（半径 8 cm），1 个目标说话人（0 度方位角）和 5 个干扰说话人；使用 gpuRIR 生成房间脉冲响应；T60 0.2-0.5 s；16 kHz 采样；STFT 512 FFT、32 ms 窗、16 ms 跳；每个混合信号取 6 秒。
- 训练：Adam，batch size 1，学习率 10^-3，250 个 epoch，损失函数为 -SI-SDR；保留验证损失最低的检查点。
- 指标：SI-SDR、PESQ、STOI，以及参数量和计算复杂度（密集层 MACs、脉冲驱动层 SynOps；直接编码下额外报告有效 MAC 率）。

## 实验结果
- 表 2 报告了 FC-SNN（direct 和 rate 编码）与 FC-ANN、FT-JNF 基线的性能。
- 直接编码（N=20）下，FC-SNN 随隐藏宽度 H 从 64、128 到 256 增长，参数量分别为 3.1K、10.3K、37.0K，SI-SDR 为 2.79、3.14、3.42 dB，PESQ 为 1.538、1.550、1.607，STOI 为 0.797、0.805、0.813；H=512 时收敛失败。
- 速率编码（N=100）下，同样 H 增长时 SI-SDR 仅为 0.78、1.07、1.21、1.28 dB，明显低于直接编码，说明事件驱动计算与增强性能之间存在清晰权衡。
- FC-ANN 在同等参数量下 SI-SDR 更高（例如 H=256、37.0K 参数时为 5.07 dB）；FT-JNF 性能最佳（H=128、310.5K 参数时 SI-SDR 7.83 dB、PESQ 2.019、STOI 0.900），但参数量远大于 FC-SNN。
- 直接编码优于速率编码，但其第一层为密集计算，可通过有效 MAC 率衡量实际成本。

## 一句话评价
该工作首次探索全脉冲神经网络用于多通道语音增强，通过顺序脉冲编码和紧凑 FC-SNN 在边缘部署的能效与性能之间取得平衡，但当前性能仍落后于 ANN 和传统波束成形基线，需要进一步优化。

---

## 19. RefTAG: Reflection-aware Temporal Audio Grounding in Large Audio Language Models

**作者**: Yuhang Dai, Xin Shu, Zhennan Lin, Mingchen Shao, Chengyou Wang, Xiangang Li, Jianwei Yu, Lei Xie
**链接**: [2610.16217](https://arxiv.org/abs/2610.16217)
**分类**: Temporal Audio Grounding | **关键词**: Temporal Audio Grounding, Large Audio Language Models, Chain-of-Thought, Self-Reflection, Reinforcement Learning, GRPO

# RefTAG: Reflection-aware Temporal Audio Grounding in Large Audio Language Models

## 核心痛点
时间音频定位（Temporal Audio Grounding, TAG）要求定位查询目标在音频中出现的**所有**区间，因此「出现次数」与「区间边界」都至关重要。然而现有 LALM 的时间定位存在两个耦合的难题：
1. **错误类型异质**：漏检某次出现（occurrence error）与边界不准（boundary error）需要不同的干预策略——移动边界无法找回被遗漏的出现，而增补区间也无法修正错误的端点。TAG-Bench 报告了重复目标上的漏计（under-counting），事件存在性分析也发现多事件场景下可靠性下降。
2. **评价不可验证**：流畅的文本式「反思批评」并不能衡量定位是否真正改善；仅做最终答案监督无法区分「有用的修订」与「对正确草稿的保留」。两个错误预测在重叠度、计数、边界精度上也可能不同。因此反思必须**明确指定修正内容并量化其效果**。

## 方法创新
本文提出 **RefTAG**，一个用于可验证时间自纠正的后训练（post-training）框架，包含以下关键设计：

- **Reflection Chain-of-Thought（Re-CoT）协议**：每条响应固定为「草稿—诊断—修订」结构，包含 `<draft>` 初始区间、离散的 **count 动作**（keep/add/remove）与 **boundary 动作**（keep/left/right/expand/shrink/adjust），以及 `</think>` 之后的修订区间。固定字段使草稿与修订可被确定性解析，从而用**统一质量函数**评估二者，无需自由文本评判器。
- **两阶段训练**：
  - **Re-CoT-SFT**：在包含草稿、诊断、修订的轨迹上做监督微调，教会模型该协议；
  - **Re-CoT-SFT-RL**：继续用 **reflection-aware GRPO** 进行强化学习，对最终定位质量与修订结果（包括对高质量草稿的保留）联合奖励。
- **共享质量函数 Q**：综合四项指标——并集 IoU（coverage）、最大一对一区间匹配（matching）、中点 MAE（midpoint accuracy）、计数一致性（count agreement），均在 [0,1] 内。
- **反思奖励 R_ref**：基于 ΔQ = Q_fin − Q_dft 的精确比较分段给分（ΔQ>0 得 0.50；ΔQ=0 且 Q_dft>0.75 得 0.25；ΔQ=0 且 Q_dft≤0.75 得 −0.10；ΔQ<0 得 −0.25），奖励改进与保留、惩罚有害修订。最终奖励为 R = α·R_fin + (1−α)·R_ref，最终模型取 α=0.3。
- **数据构造**：以真值条件化的 LLM 生成候选 Re-CoT 轨迹，再用确定性规则做后处理与平衡（边界 keep 要求计数相等、并集 IoU≥0.70、匹配 IoU≥0.60 等），得到 **275,000** 条平衡轨迹；并从中选取 **5,000** 条（按查询类型、时长、目标数量平衡）用于 RL 子集。真值只用于数据构造与奖励，从不进入推理。
- **推理无需额外标注**，主干网络不变，也不需要检索系统或局部音频工具循环。

## 实验结果
- Re-CoT-SFT 相比仅最终答案的 SFT，在 8,228 条查询上将 query-weighted mIoU 提升 **1.74 个百分点**。
- RL 进一步将 TAG-Bench 多目标 mIoU 提升 **0.40** 点，R@0.5 提升 **0.86** 点。
- 最终模型（Re-CoT-SFT-RL, α=0.3）达到 **38.50% TAG-Bench mIoU** 与跨三个数据集（Clotho、LAT、TAG-Bench）的 **51.01% 平均 mIoU**。
- 在上述两项指标上均**优于**开源模型 MOSS-Audio-8B-Thinking（34.24% Avg）与 FireRedAudio（37.76% Avg），以及商用模型 Gemini-3.1-Pro（42.52% Avg）。
- 实验拆分了最终精度、草稿信息量与修订增益，并测试了奖励混合与各质量分量的作用。

## 一句话评价
RefTAG 通过将「草稿—计数/边界诊断—修订」的反思链显式结构化，并用联合奖励优化把中间反思过程与定位目标直接挂钩，为时间音频定位提供了一条**可验证、可度量**的自纠正路径。

---

## 20. FOAdapter: A Plug-and-Play Spatial Tokenizer for Low-Bitrate FOA Speech Coding

**作者**: Kirak Kim, Yoonjeong Park, Juhan Nam, Sungyoung Kim, Minje Kim
**链接**: [2610.16202](https://arxiv.org/abs/2610.16202)
**分类**: Spatial Audio Coding | **关键词**: First-Order Ambisonics (FOA), Neural Speech Coding, Spatial Tokenizer, Low-Bitrate Coding, Contrastive Learning

## 核心痛点

空间音频同时携带语言内容与空间线索，对远程会议、沉浸式媒体等应用很重要。现有神经语音编码器（NSC）在低码率单声道语音重建上表现优异，但大多针对单声道/立体声，不显式编码 FOA 四通道空间结构。将单声道 tokenizer 简单扩展到 FOA 的通道独立方案会使总码率翻四倍，且低码率下空间线索受损。已有工作如 SpatialCodec 面向 8 通道麦克风阵列且总码率约 12 kbps；FOA Tokenizer 虽在 0.9 kbps 联合编码 FOA，但在其内部 SpatialVCTK 上 WER 达 67%，语音内容保持仍有提升空间。因此核心问题是：能否利用预训练单声道 tokenizer 实现低码率 FOA 语音编码，同时保持语音内容和空间信息？

## 方法创新

提出 FOAdapter：一个即插即用（plug-and-play）的因果空间适配器/空间 tokenizer，基于冻结的预训练单声道语音 codec 完成 FOA 编码。整体框架只用解码后的 W 通道加一条独立的低码率空间 token 流来重建完整 FOA，目标总码率约 1.5 kbps，空间流为 275 bit/s。

- 单声道 codec 编码 W：z_m = Q_m(E_m(W))，W_hat = D_m(z_m)。
- FOAdapter 由因果卷积编码器 E_s、量化器 Q_s 和解码器 D_s 组成，从完整 FOA 信号 S=[W,X,Y,Z]^T 提取空间 token：z_s = Q_s(E_s(S))。
- 空间解码器 D_s 以 z_s 为条件重建 S_hat = D_s(z_s, W)。训练时条件 W 使用真值 W，推理时使用解码 W_hat，从而避免适配器绑定到某个特定单声道 codec，提升跨 codec 兼容性。
- 空间 token 使用两层 RVQ，每层 2048 个码本条目，12.5 tokens/s，额外码率 R_s = 2×12.5×log2(2048)=275 bit/s；总码率为 R_m+R_s。
- 空间解码器采用波形特征提取器 F_W 和空间上采样/调制网络 U_s，以 FiLM 变体调制特征：h_W_tilde = h_W ⊙ (1+0.5 tanh(gamma)) + beta，再由 G_s 输出四通道 FOA。
- 空间表示学习结合直接空间监督与空间对比学习：辅助头从空间 token 预测 intensity direction 和 log intensity magnitude，构成 L_aux；对比学习用同一录制中两个 2 秒片段作为正对，用方向差异超过 5° 的其他样本作为负对，并用同一话语的其他空间渲染作为 hard negative，以 InfoNCE 优化 L_con，使空间 token 对同一方向相似、对不同方向可区分。
- 训练损失为七项加权和：L_G = λ1 L_rec + λ2 L_aux + λ3 L_sc + λ4 L_con + λ5 L_adv + λ6 L_fm + λ7 L_vq。其中 L_rec 为四通道波形 L1 与多分辨率 STFT 损失；L_sc 为 FOA Tokenizer 中的 diffuseness-weighted spatial-consistency loss；判别器沿用 HiFi-GAN 多尺度/多周期设计，含通道独立判别器与联合判别器，提供 hinge adversarial 和归一化 feature-matching 损失；L_vq 为 codebook 与 commitment 损失。

## 实验与结果

- 数据：Spatial LibriSpeech。训练使用 8,504 个房间的 163,345 条录音（544.53 小时），保留 5% 训练房间做验证；测试使用官方 49,505 条空间化录音、73 位说话人、4,970 个模拟房间（85.49 小时）。训练时随机采样与 token 对齐的 4 秒片段，并将 16 kHz 重采样到 24 kHz 以匹配预训练单声道 codec。数据增强包括对四通道施加 [-6,6] dB 共享增益，以及对方向通道和 DOA 元数据联合施加随机 3D 旋转。
- 实现：空间编码器/解码器为五级因果卷积，采样因子 [8,6,5,4,2]，隐层维度 384，空间分支 28.84M 参数；采用 DAC 的改进 RVQ；冻结单声道 tokenizer，从头训练空间分支 250k generator updates，batch size 8，AdamW 峰值学习率 1e-4 并 cosine decay；训练 50k updates 后加入对抗训练，对抗与 feature-matching 权重在后续 10k updates 线性增加。
- 基线：通道独立（CI）编码，包括 DAC-1/2/8、Mimi-8、MOSS-3/8，后缀为码本数；Opus mapping family 2 总码率 24 kbps；MPEG-H 3D Audio HOA 128 kbps 作为高码率参考。所有单声道 codec 共用同一个 FOAdapter checkpoint，不重新训练。FOA Tokenizer 因代码和预训练模型未公开而未参与比较。
- 指标：空间保真度用 RTF error（弧度）和 MUSIC-based DOA error（方位角、仰角、总角度，度）；语音质量/可懂度在波束形成后的单声道信号上用 UTMOS、PESQ、SNR、STOI；WER 用 Whisper-large-v3。
- 主观：27 人参与 MUSHRA-inspired 听音测试，8 段来自 Spatial LibriSpeech test-clean，评价整体语音质量以及感知声源方向与参考的一致性。
- 主要结果：FOAdapter 在所有评估的预训练单声道 codec 上都能一致地保留空间信息，使用 275 bit/s 空间流即可取得约 7° 的 DOA error；在不同 codec 上 DOA error 约 7°，但在语音重建质量上存在 trade-off。token-swapping 实验表明空间 token 流主要独立于语音内容地携带声源方向信息。听音测试显示其感知语音质量高于同码率量级的通道独立基线。

## 一句话评价

FOAdapter 通过冻结单声道 codec 加 275 bit/s 空间 token 流和空间对比/监督学习，为 FOA 语音提供即插即用的低码率空间编码方案，在约 7° DOA 误差下显著补足现有单声道神经语音编码器的空间线索保持能力，代价是语音重建质量有一定折衷。

---

## 21. Towards Privacy-Preserving ASR: Speaker-Level Machine Unlearning

**作者**: Seaone Ok, Seungu Han, Eungbeom Kim, Kyogu Lee
**链接**: [2610.16196](https://arxiv.org/abs/2610.16196)
**分类**: Speech Recognition (ASR Machine Unlearning) | **关键词**: Machine Unlearning, Automatic Speech Recognition, Speaker-Level Unlearning, Privacy Preservation, Self-Supervised Learning, HuBERT, Membership Inference Attack, Representation-Level Unlearning, Speech-Aware Identity Dispersion

# 论文总结：Towards Privacy-Preserving ASR: Speaker-Level Machine Unlearning

## 核心痛点
- ASR 通常被设计为说话人无关的转写系统，但现代 ASR/SSL 模型（如 HuBERT）的潜在表示中仍会编码说话人身份、口音等副语言信息，形成残留声学指纹。
- 在模型微调尤其是临床、低资源等小数据场景中，这类说话人信息可被成员推理攻击利用，判断某说话人是否在训练集中，引发 GDPR 被遗忘权等合规与隐私风险。
- 在 ASR 上做说话人级遗忘很困难：语音表示中语言内容与说话人信息高度耦合；简单遗忘会损害通用转写能力；现有 ASR 遗忘工作多关注样本级遗忘或训练时抑制目标说话人转写，尚未解决在保持转写性能的同时擦除说话人身份的问题。

## 方法创新
1. 层级分析：对基于自监督学习（SSL）的 ASR 表示做逐层分析，发现说话人身份主要编码在编码器中间层（论文选择第 6 层）。
2. 辅助说话人表示头：在 HuBERT-base 编码器第 6 层隐状态上接一个说话人分类头，冻结编码器先训练该头，得到可控的说话人嵌入空间 z，便于在表示层干预且尽量不破坏 ASR 解码器依赖的语言表示。
3. 表示级遗忘目标：总损失为 `Ltotal = Lctc(Dr) + λ Lunlearn`，其中 CTC 损失只在 retain 集上计算，forget 集被当作非成员数据，不显式优化其 CTC；λ=1。
4. SAID（Speech-Aware Identity Dispersion）：两阶段说话人感知身份分散。阶段一用 K-Means 对 forget speakers 的嵌入聚类，估计每个说话人分布的中心 c_s；阶段二解冻编码器，用基于 margin 的分散损失把 forget 样本嵌入推离对应中心：`LSAID = softplus((cos(Ψθ(xj), c_s) - m) / τ)`，其中 m 为距离 margin，τ 为温度系数。
5. 该目标在潜在空间中分散说话人特定簇，而不是仅做参数更新、梯度上升、标签破坏、蒸馏或结构编辑，从而在擦除说话人身份的同时保留语言表示。

## 实验与结果
- 数据集：VCTK 多说话人英语朗读语料，使用 mic2 录音，剔除 p280 和 p315，共 108 位说话人，重采样到 16kHz。
- 划分：随机分为 retain 集 Dr=95 说话人、forget 集 Df=5 说话人、test 集 Dt=8 说话人；训练/评估按 9:1 划分；保持性别和口音平衡；说话人身份在训练和评估间严格不重叠。
- 参考模型：HuBERT-base + CTC。Original Model 在 Dr,train ∪ Df,train 上训练；Gold Model 仅在 Dr,train 上训练，用于模拟完全重训练后的理想遗忘模型。
- 说话人头：接在第 6 层，用交叉熵训练 15 epochs，学习率 3×10−4，训练时冻结 ASR 编码器；所有遗忘方法共享相同配置。
- 结果：在 VCTK 上，所提方法能移除特定说话人的影响，同时保持稳健的转写性能；相比现有遗忘基线取得更好的隐私-效用权衡。片段未给出具体 WER、MIA 准确率等数值。

## 一句话评价
该工作较早地将说话人级机器遗忘引入 ASR，通过中间层说话人表示空间与 SAID 质心分散损失，在 VCTK 上初步实现了隐私擦除与转写性能之间的可行折中，是隐私保护 ASR 的一个有前景的方向。

---

## 22. Unsupervised Cross-device Speaker Diarization And Linking Through Spatiotemporal Structure

**作者**: Suhas BN, Nikitha K
**链接**: [2610.15978](https://arxiv.org/abs/2610.15978)
**分类**: Cross-device Speaker Diarization and Linking | **关键词**: cross-device speaker linking, speaker diarization, constrained clustering, speaker embeddings, clinical workflow

## 论文信息
- **标题**: Unsupervised Cross-device Speaker Diarization And Linking Through Spatiotemporal Structure
- **作者**: Suhas BN, Nikitha K（Independent Researchers）
- **任务**: 在无访客注册、无访客身份标签的模拟门诊工作流中，跨独立房间/设备链接同一访客的语音。

## 核心痛点
- 跨房间/跨设备场景下，麦克风、房间声学与编解码器不匹配会严重扭曲说话人 embedding，使聚类反映录音设备特征而非说话人身份；这与单录音内 diarization 不同。
- 设施日程提供额外结构信息：同一人不能同时出现在两个房间；某些房间类型最多一次访问，但返访会破坏该规则；已识别 staff 在多录音器上出现可提供跨设备校准。
- 预处理问题关键：跨房间重复语音（同一 utterance 被多个录音器拾取）必须去除；电视等媒体需拒绝。没有去除跨房间重复语音时，方法仅在 2/11 个 extractor 上胜出。
- 单次访问患者仍容易被错误合并（false merge），日程约束本身无法解决 singleton identity 错误。

## 方法创新
1. **设备中心化（per-device embedding centering）**：对每个录音器计算全天平均 embedding µ_d，从访客的 chunk embedding 中减去该录音器均值后再归一化形成 centroid，以降低录音器共享偏移；不需要访客标注自适应数据。
2. **房间类型感知约束（room-type-aware constraints）**：构建 cannot-link 集合 C。并发约束：不同房间、同一时间槽的观测不能是同一身份，前提是它们是不同访问而非重复音频。房间唯一性约束：仅对协议规定不能返访的房间子集 R_once，将同一房间的观测设为不同身份；其他房间允许返访，避免把工作流假设当成通用身份规则。
3. **基于日程与 staff 的阈值校准**：并发访客对提供负余弦分数；同一已识别 staff 成员在不同录音器上的语音提供正分数。阈值 τ 取两组分数经验 EER 工作点。
4. **约束 AHC 聚类**：average-linkage 凝聚聚类，从每个观测一簇开始，每步合并 admissible 且平均跨簇余弦相似度最大、不低于 τ 的 pair；若合并会使任意组成 pair 落入 C 则不可合并。无需指定访客数量。
5. 评估变体包括 concurrency-only、全房间 same-room 规则、泄漏 guard、使用前一天统计、在线 causal greedy 链接。

## 实验设置
- 数据：VOiCES 在真实房间重录 LibriSpeech；选 100 名测试说话人，性别平衡，含近/远麦克风及 quiet/babble 条件；加入类电话处理（AGC + Opus 12 kb/s 或 8 kHz GSM 06.10）。
- 默认模拟日：40 患者、4 房间、4 staff、每次说话访问 6 秒、3 秒 chunk；hard recorder mix 含 Opus、带 babble 近麦、远麦和 GSM；20 个模拟日。现实工作流含 companions 70%、实验室返访 85%、silent visit 20%、跨房间泄漏 15%、walk-ins 15%、电视 50% 时间槽。
- 11 个冻结 extractor，覆盖 5 个家族，参数量从 1.1M 到 587M，包括 ECAPA-TDNN、TitaNet、ERes2Net、ReDimNet2 系列和 w2v-BERT 2.0 SV；9 个紧凑模型经 ONNX CPU 推理，论文未报告统一 runtime/latency。
- 基线：AHC、PLDA adaptation、NME-SC，raw 或 centered embedding；label-free 方法不利用访客身份标签选阈值；oracle-informed 使用标签调优阈值或真实人数，仅作特权参考。
- 指标：visit-level B3 precision/recall/F1（×100）、精确 itinerary 恢复率、单次访问患者错误合并率、20 个模拟日上的 95% t 区间。

## 主要结果
- 默认模拟日上，所有 11 个 extractor 相比最佳 label-free 基线提升 5.3–14.6 B3-F1 点，中位配对增益 8.3，全部增益显著；其中 TitaNet 的最大增益受训练数据可能重叠的 caveat 影响。
- ECAPA-TDNN：提出方法 86.6 B3-F1，最佳 label-free 基线 76.4，centered AHC + oracle 阈值 87.7；精确 itinerary 恢复从 label-free centered PLDA 的 41% 提升到 57%。
- 与 oracle-informed 基线相比，提出方法中位差距 1.9 点；对 2 个 extractor 超过 oracle 参考但不显著，对 ECAPA-TDNN 统计不可区分，对剩余 8 个显著更低。
- 更强/更广训练的表示仍有效：w2v-BERT 达到 93.1 F1、76% itinerary；ReDimNet2-B3 达到 92.1、73%；1.1M 的 ReDimNet2-B0 从 79.2 提升到 84.5，但未超过最强未修改 extractor。结构信息补充表示质量，而非替代。
- 消融/变体：将 same-room 规则应用到所有房间使 ECAPA-TDNN F1 从 86.6 降至 78.2，说明返访被错误排除；concurrency-only 仅 68.3；room-type-aware + leakage guard 86.9；yesterday statistics 86.3；online causal greedy 82.2。
- 失败模式：方法高度依赖去除跨房间重复语音；没有该预处理仅 2/11 extractor 获胜。单次访问患者 false merge 比例仍高（Table 1 中 35%–72%）。日程约束单独无法解决重复语音和 singleton identity 错误。

## 一句话评价
该工作用设备中心化、房间类型感知时空约束和 staff 校准阈值，在无访客标签的模拟门诊跨设备说话人链接中显著优于 label-free 基线，但重复语音与单次访问身份安全仍是临床部署前的关键障碍。

## 局限
- 实验为模拟工作流，并非真实临床录音，结论外推需谨慎。
- 需要共同时间槽参考；时钟错误和残余声学泄漏可破坏并发约束。
- 未报告所有 11 个模型的统一运行时间/延迟；TitaNet 训练集含 LibriSpeech，可能与评估说话人重叠。
- 单次访问患者和跨房间重复语音问题未完全解决。

---

## 23. Controllable Mono-to-Stereo Upmixing using Reward-tilted Flows

**作者**: Sattwik Basu, Gautam Bhattacharya, Alan Seefeldt
**链接**: [2610.15967](https://arxiv.org/abs/2610.15967)
**分类**: Audio Upmixing | **关键词**: mono-to-stereo upmixing, flow matching, reward-tilting, generative inverse problems, spatial audio control, audio restoration

## 核心痛点
- 单声道到立体声上混（mono-to-stereo upmixing）本质是不适定逆问题：同一单声道可由多个立体声信号下混得到，单声道缺少声道间空间线索。
- 现有方法分为信号处理、端到端生成和参数化方法：信号处理方法依赖时延、去相关、多频带处理或源-环境分解；生成方法如 DiffStereo 需要任务特定训练；参数化方法可解释但输出受限。
- 主要不足：手工空间规则、任务特定训练/微调、输出参数化受限，且难以在推理时提供可控空间成像。

## 方法创新
- 提出 Aura（Audio Upmixing using Reward-tilted Flows），将上混重写为生成式逆问题，使用预训练 flow 模型作为立体声音频先验 p(x)。
- 测量模型：y=A(x)+n，A=D∘M，M 为立体声到单声道下混，D 为可选退化算子。通过组合前向算子，可在不重训/微调的情况下同时做恢复与上混。
- 后验采样：从 p(x0|y) ∝ p(y|x0)p(x0) 采样；使用 flow 的 Tweedie 估计 x̂0(xt)=xt−t vθ(xt,t)，并以高斯近似先验 p(x0|xt)。
- 奖励倾斜：设计空间奖励 r_sp(x0)，通过 KL 正则化奖励最大化得到指数倾斜后验 p̃(x0|xt,y) ∝ p(x0|y,xt) exp(r_sp(x0)/β)，在保持测量一致性的同时控制空间属性。
- 两阶段解耦精修：先求测量一致估计 x*0（数据保真+先验邻近），再在信任域内最大化空间奖励，得到近端精修目标 x†0=argmin{−r_sp(x0)/β + (η/2)||x0−x*0||²}，避免非凸奖励与测量一致性联合优化不稳定。
- 空间奖励设计：在 ERB 感知频带内计算空间协方差矩阵 SCM，并提取 IC（声道间相干性）与 ILD（声道间电平差）随时间分布；IC 用 Beta 分布建模，ILD 用高斯分布建模，通过矩匹配从参考片段估计目标参数，无需成对监督。

## 实验结果
- 在 MUSDB18-HQ 真实音乐录音上评估，包括干净单声道下混和受带宽损失、削波、加性噪声退化的观测。
- 评价包括重建准确度、频谱保真度、空间真实感等客观指标，以及感知质量和立体声声像的主观听音测试。
- 摘要与引言称相对多种信号处理、参数化和学习生成基线取得改进；片段未给出具体数值表格。
- 论文还讨论了方法可推广到单声道到立体声之外，并对环绕声生成给出初步思考。

## 一句话评价
Aura 用预训练 flow 先验把单声道到立体声上混建模为可奖励倾斜的后验采样问题，以训练-free、可控空间成像和可组合退化算子为核心卖点，为音频上混提供了兼具生成质量与推理时控制的新范式。

---

## 24. High-Fidelity Song Generation with Joint Discrete and Continuous Modeling

**作者**: Zheqi Dai, Zhiyue Wu, Ruibin Yuan, Haolin He, Chunyat Wu, Xuerui Yang, Qiuqiang Kong, Chao Yan
**链接**: [2610.15802](https://arxiv.org/abs/2610.15802)
**分类**: Song Generation (Text-to-Music / Lyrics-to-Song Generation) | **关键词**: Song Generation, Joint Discrete and Continuous Modeling, Flow Matching, Semantic Tokens, Autoregressive Language Model, Vector Quantization, Text-to-Music

## 核心痛点

从歌词与风格描述生成完整歌曲，需要在不牺牲人声与伴奏细节的前提下进行分钟级的音乐规划（长程结构、旋律、编曲）。

现有范式存在两个根本性瓶颈：

1. **量化信息损失**：低帧率离散语义 token 让长序列规划变得可行，但向量量化会把不同的自监督音乐特征映射到同一 token，查表返回的连续向量无法恢复在分配阶段丢失的差异，限制了送入声学渲染器的语义信息量。
2. **分阶段训练目标割裂**：语言模型以「下一 token 交叉熵」训练，下游扩散/流匹配渲染器以「合成音频」为目标独立训练。当唯一的连接是采样出的 token ID 时，合成目标无法反向更新产生这些 token 的语言模型参数——token 预测并未针对最终音频保真度做联合优化，生成歌曲因此可能残留可感知的音频伪影。

核心问题：**如何在不放弃可处理的离散规划的前提下，丰富「规划」与「声学渲染」之间的信息通道？**

## 方法创新

受 DisCon（离散图像预测可引导连续空间生成）启发，论文提出 **联合离散与连续建模（Joint Discrete and Continuous Modeling, JDCM）**，在 SSL 初始化的音乐编码器上构建两条对齐的表征分支：

- **离散分支**：VQ tokenizer 提供自回归语言模型的离散语义 token 规划（25 Hz、单码本）。
- **连续分支**：单独训练的变分编码器（SSL-derived variational encoder）提供连续语义目标 s = (s₁,…,s_T) ∈ R^{T×D}，其帧与离散 token 对齐，但 s_t 既不是 VQ 分支的量化前特征 u_t，也不是码本向量 e_t。该编码器通过歌词转写监督、mel/chroma 重建、与冻结 SSL 教师的对齐以及 KL 正则共同训练，以保留人声内容、频谱与和声信息；联合训练前被冻结。
- **全序列语义流（semantic flow）**：以「完整的 token 规划」+「语言模型因果预测状态的可微 readout」为条件，生成连续语义特征，再由声学渲染器转成音频。
- **关键机制**：流匹配（flow-matching）梯度经由 readout 回流到语言模型，与 token 交叉熵并列更新规划器，且**无需对硬 token 采样求导**。标准路径保持离散 token 作为语言模型唯一的自回归反馈，连续特征不进入自回归历史。
- **Joint-SB 交错变体**：探索把生成的连续语义特征回灌到后续规划中（在连续语义空间做反馈），但这会引入训练用参考特征、推理用生成特征之间的 exposure bias；标准路径避免了这一特定失配。

论文的三点贡献：(1) 联合离散+连续建模的整曲生成方法，让流匹配目标能更新规划器；(2) 在方法内部横向比较语义瓶颈宽度（如 48D）、目标空间与生成框架（全序列语义合成、直接声学潜变量预测、交错语义反馈）；(3) 通过 MARBLE 探针、100 首内部歌曲的源条件重建等中间诊断，将表征层面与生成层面的分析关联到客观指标与专家听感结果。

## 实验结果

- 在 **192 条共享 WildSongBench prompts** 上，评测 6 个系统，采用客观质量与风格指标、由转写导出的音素错误率（micro-PER），以及由 5 位音乐专家对 10 组匹配歌曲进行的听测。
- **48D 配置**相对离散基线：
  - SongEval 从 **4.152 → 4.269**
  - micro-PER 从 **20.26% → 14.47%**
  - 专家听感评分显著更高
- 联合建模家族在主要客观指标与听感指标上整体占优，不同配置各有取舍。
- 使用 MARBLE 探针与源条件重建作为中间诊断，强调参考条件分数不一定能预测自由生成表现。

## 一句话评价

论文以「离散 token 规划 + 连续语义流渲染、梯度经可微 readout 回流」的联合训练框架，巧妙绕开量化信息瓶颈与阶段割裂问题，在不引入 token 采样求导与自回归反馈污染的前提下，同时取得客观指标与专家听感的双重提升，为长曲式歌曲生成提供了简洁而有效的建模范式。

代码与演示：https://dzq84.github.io/JDCM/

---

## 25. HMU-Bench: Hierarchical Music Understanding Benchmark for Omni Models

**作者**: Zheqi Dai, Boyang Wang, Zhiyue Wu, Yiyang Xu, Xinming Shi, Ruibin Yuan, Xuerui Yang, Chao Yan, Qiuqiang Kong
**链接**: [2610.15773](https://arxiv.org/abs/2610.15773)
**分类**: Music Understanding Evaluation / Multimodal Audio-Language Benchmark (MIR) | **关键词**: music understanding, omni models, hierarchical benchmark, ABC notation, audio question answering

# HMU-Bench: 面向 Omni 模型的分层音乐理解基准

## 核心痛点

现有音乐理解基准通常只报一个总分，既没有说明**模型能看到什么证据（evidence）**，也没有说明**一个正确答案需要执行什么操作（operations）**。这导致两类问题：

1. **无法定位失败原因**：总分低时，难以区分是模型听不出音符/和弦，还是无法完成多步音乐推理。
2. **模态混淆**：Omni 模型同时接受音频与文本/符号输入，但符号（乐谱）侧与音频侧的能力往往被混合评估，掩盖了「识谱强、听音弱」这类结构性缺陷。
3. **评估器本身的可靠性未被检验**：论文通过移调（transposition）案例研究发现，LLM 打分器会漏掉符号输出中的**八度（octave）错误**，说明纯 LLM 评分存在盲区。

## 方法创新

### 1. 两部分、双语、分层标注的基准（Benchmark）

- **ABC Q&A（符号侧）**：1,029 组中英双语问答题对，覆盖 **6 个音乐领域、38 种任务类型**，每题带「解题要求」标签：
  - `extraction (e)`：直接读取乐谱中编码的属性（如休止符后的进入拍）。
  - `single-step inference (1)`：施加单一音乐关系（如 K:E 下 C♯–B 为上行小七度）。
  - `multi-step inference (n)`：链式推理（如先做等音重解，再解释其解决与声部进行）。
  - 标签描述的是**预期的解题要求，而非校准过的难度**。
- **Audio Q&A（音频侧）**：460 组中英双语问答题对，来自 **92 段录音**，交叉组合「全局/局部 scope」与「easy/medium/hard 难度」，形成 5 种配置（global/easy、global/hard、local/easy、local/medium、local/hard），每配置 92 题（共 184 全局 + 276 局部）。
- 答案均为**开放式**，可包含解释或重写后的乐谱（notation），而非选择题。

### 2. 证据链式构建流程（Construction Pipeline）

- **ABC 池**：997 首 Suno 生成歌曲，用 SheetSage2 自动转写；对齐旋律事件到时值与节拍，归一化和弦符号、行内调性变化与延音线；任务化摘录保留音高拼写、音区、时值、休止、拍号与必要和声语境，去除歌词、描述性段落名与自由注释，减少无关文本线索。
- **音频集**：92 段 Suno 录音，人工听辨并标注/修正和弦与段落边界；修正后的和弦用于调整 SheetSage2 的 ABC 转写。注释与修正乐谱既作为出题证据，也用于构造参考答案；段落边界定义 local 题的窗口。
- **出题与校验**：ABC 题与参考答案由 GPT-5.6 Sol（ultra reasoning 设置）起草；音频题由人工模板实例化，参考答案直接取自人工标注。所有题目经人工审查（措辞、音乐正确性、题干/证据/参考答案一致性），英文版在同一证据上生成。最终 ABC 集为 997 首歌、1,166 段摘录、1,029 组题对：335 extraction / 441 single-step / 253 multi-step。

### 3. 统一评分协议（Evaluation Protocol）

- ABC 查询 = 中/英文题干 + 乐谱摘录（两语言共享同一乐谱，便于语言对照）；音频查询 = 完整录音 + 题干，local 题额外给出目标段落、时间窗与小节范围，完整录音仍作为上下文。**参考答案与评分标准从不展示给作答模型**。
- 由 Qwen 3.5 Flash 打分：ABC 题打分器额外可见乐谱；音频题可见结构化答案键与文本注释证据，但**不可听录音**。
- 整数 0–4 分：0 错误/无支撑/缺失；1 基本错误但有少量相关内容；2 部分正确但有重要错误或遗漏；3 核心结论正确但有细节遗漏；4 完整正确。音乐等价表达可接受；缺失必需解释或组成项不得满分。
- 指标：平均分 $\bar{s}=\frac{1}{N}\sum_i s_i$，音频额外报告满分率 $FCR=\frac{100}{N}\sum_i \mathbb{I}[s_i=4]$。中英分开报告，子组分数聚合两语言。评分后由人工审计分数与评分理由，约 20 条参考模糊或证据不足的题被修订并重评。

## 实验结果

**评测规模**：7 个 omni 模型（Gemini 3.7 Flash、Gemini 3.1 Pro、Gemini 2.5 Pro、Seed2.0 Lite、Qwen 3.5 Omni Plus、Qwen 3 Omni Flash、StepAudio 3 Realtime），另加 2 个纯文本参照系统（GPT-6 Astra、DeepSeek V4.1 Flash，仅参与 ABC Q&A）。共评分 **18,522 条 ABC 回答**（1,029 题对 × 2 语言 × 9 模型）与 **6,440 条音频回答**（460 题对 × 2 语言 × 7 模型）。

### ABC（符号）Q&A
- Gemini 3.7 Flash 在 omni 模型中领先（ZH/EN = 3.840/3.864），其后为 Seed Lite（3.516/3.521）与 StepAudio 3（3.306/3.408）；纯文本 GPT-6 Astra 达 3.964/3.945。
- Gemini 3.7 Flash 在所有领域均为 omni 最高；**所有 omni 模型都在 global information 上得分最高，而 pitch and melody 是最弱领域**。
- 文字参照系统表现突出，说明符号乐谱题对文本模型相当友好。

### Audio（音频）Q&A
- **没有任何模型在 0–4 音频量表上平均分超过 1.4**；最高为 Qwen 3.5 Omni（1.330/1.333），其后 Gemini 3.1 Pro（1.176/1.122）、Gemini 3.7 Flash（1.159/1.028）等，最低为 Gemini 2.5 Pro（0.917/0.898）。
- 满分率随难度陡降：global/easy 最高约 48.4%（Qwen 3.5 Omni），global/hard 与 local/hard 普遍低于 5%，**local/hard 上多数模型 FCR 为 0**。
- 符号与音频排名**几乎不相关**：符号强不代表听得懂音乐。

### 关键发现
1. 符号能力与音频能力解耦，应**分模态报告**。
2. 音频侧整体能力仍处于低位，尤以细粒度 local / hard 听觉推理为瓶颈。
3. 移调案例研究显示 LLM 打分器会漏检符号输出中的**八度错误**，因此符号输出需要**事件级（event-level）检查**，而不能只依赖 LLM 打分。

## 一句话评价

HMU-Bench 用「证据 + 解题操作」的双重分层标注，把音乐理解拆解为可解释的符号与音频两条评测线，首次系统揭示 omni 模型「识谱尚可、听音极弱」且两模态排名脱节的现实，并警示 LLM 打分在符号输出上会漏掉八度级错误——是一个兼具诊断力与批判性的音乐理解基准。

---

## 26. The NPU-ASLP System for Music Restoration in the CCF-AATC 2026 Challenge

**作者**: Zeyu Zhu, Yike Zhu, Xingchen Li, Chaoren Yu, Jingyi Wang, Yurun Li, Jierui Guo, Chunjiang He, Lei Xie
**链接**: [2610.15464](https://arxiv.org/abs/2610.15464)
**分类**: Music Restoration | **关键词**: Music Restoration, Mixture of Experts, Complex Spectral Mapping, Acoustic Simulation, Audio Enhancement, TF-MoE, Scale-Aware Encoding

## 核心痛点
- 任务目标：从移动设备录制的音乐中恢复干净音乐，退化来自播放设备、声学传播、环境噪声与录音终端，且这些退化在单一观测中相互耦合。
- 退化特点：扬声器染色与非线性、距离衰减、混响、环境干扰、麦克风响应和增益控制同时作用，部分退化直接作用于频带能量，导致绝对尺度与跨频带电平线索严重削弱。
- 音乐复杂性：音乐包含宽带谐波、精细泛音、打击瞬态、人声与多样乐器，恢复需要同时建模精细复频谱结构与跨频带能量关系。
- 数据约束：官方仅提供约10 h真实配对数据，且部分输入与目标存在不可忽略的时间偏移，平均绝对延迟89 ms，80%配对的延迟超过20 ms，污染样本对齐的频谱监督。
- 效率约束：挑战赛有严格参数量与计算量预算，官方AudioFlow基线虽可行但550.87M参数、4.49T MACs过于庞大。

## 方法创新
1. 骨干模型：以TF-MoE为恢复骨干，利用频带轴和时间轴的双轴建模能力捕捉跨频带与时间依赖；Top-1路由每个token只激活一个专家，在严格预算下限制计算量。
2. 尺度感知频带编码器：替换传统频带归一化，将归一化复频谱与每频带log-RMS联合编码；一路用每频带RMS归一化保留相位与频带内相对结构，另一路提供对数压缩RMS以显式保留频带能量尺度。
3. 复频谱映射解码器：直接估计干净复频谱的实部与虚部，而非预测掩蔽与输入相乘，从而更灵活地修复被强烈衰减或非线性失真的成分。
4. 双轴稀疏MoE：6个堆叠TF-MoE块，分别用频率轴F模块和时间轴T模块建模；每个模块采用Conformer风格设计，含4头自注意力、kernel-31卷积和两个MoE前馈层；每个MoE含12个两层FFN专家，扩展因子4。
5. 训练目标：多分辨率STFT损失、时域MAE损失、基于冻结VGGish的感知损失，以及Switch风格负载均衡损失；感知权重在前2000步线性预热到0.05，总损失为L_MRSTFT + 0.2L_time + λ_perc(s)L_VGGish + 0.001L_bal。
6. 挑战校准仿真管线：利用真实录音估计场景、设备、距离与电平分布，构建播放-传播-录音物理退化流程；总计202种场景-设备-质量-距离条件，每个条件采样1000个episode，生成202,000个样本对齐配对，合计1,572.121 h。
7. 仿真数据源：约10 h官方配对用于剖面分析与真实验证；180,436条精选音乐、821,144条噪声、50,000个RIR响应；噪声库包括DNS Challenge 3/5、MUSAN、TAU Urban Acoustic Scenes、FSD50K、DEMAND、UrbanSound8K、Datumo Background Noise、ESC-50、ASPED v.b、SONYC-UST及网络采集音频。
8. 预处理与上下文：从高质量音乐中选取20–36 s活跃片段，匹配官方干净RMS分布并保留3 s真实上下文前缀，使混响、压缩和AGC状态在监督段之前稳定。

## 实验结果
- 模型复杂度：最终系统2.951M参数，10 s输入需要82.659 GMACs。
- 官方盲测：-49.067 dB SI-SNR，1.273 LSD，2.540 FAD，3.495 ViSQOL。
- 排名与奖项：在LSD、FAD、ViSQOL三项指标上排名第三，获得挑战赛三等奖。

## 一句话评价
该工作通过尺度感知TF-MoE复频谱映射与大规模挑战校准仿真，在严格参数预算下有效缓解了真实配对不足、时间未对齐和耦合退化问题，取得了CCF-AATC 2026 Track 1三等奖。

---

## 27. LiveAnon: Improving Privacy and Utility in Streaming Speaker Anonymization with Codec Language Models

**作者**: Yejin Kim, Kyungsu Kim, Seungu Han, Kyogu Lee
**链接**: [2610.15379](https://arxiv.org/abs/2610.15379)
**分类**: Streaming Speaker Anonymization | **关键词**: Streaming Speaker Anonymization, Voice Conversion, Neural Audio Codec, Codec Language Model, Privacy-Utility Trade-off, RVQ Decoding, Emotion Preservation

## 核心痛点
- 说话人匿名化需要在隐藏说话人身份的同时保留语言内容与情感等副语言信息，天然存在隐私-效用权衡。
- 现有流式 SA 系统常因离散/量化内容瓶颈丢失情感信息，或需要额外的韵律建模、情感表示蒸馏、情感特定监督，增加系统复杂度。
- 流式场景还要求有限未来上下文与有界延迟，因此必须同时平衡延迟-质量以及隐私-效用。

## 方法创新
- 提出 LiveAnon：一个基于声音转换（VC）的流式说话人匿名化框架，使用自回归 codec 语言模型进行声学生成。
- 直接以预训练流式 Zipformer ASR 编码器的隐藏表示作为内容条件，分析表明该表示保留较多情感相关信息且说话人区分性较低。
- 目标身份通过前缀 codec prompt 指定：参考 codec 序列与生成序列在同一自回归声学流中继续，无需显式说话人编码器。
- 引入 capped RVQ decoding：将 MusicGen 的 delay pattern 限制为最大偏移 δ_max，保留粗粒度 codebook 之间的依赖，同时并行预测剩余 RVQ codebook，从而降低 codec 生成延迟。
- 系统使用 JHCodec 流式神经音频编解码器、因果 Transformer decoder、FiLM 条件、VALL-E 式 acoustic prompting、teacher forcing 训练，以及推理时 KV cache 预填充参考 prompt。

## 实验与结果
- 训练数据：LibriTTS train-clean-100 与 train-clean-360，约 460 小时，重采样到 16 kHz；保留至少 6 秒话语并切分为两个连续 3 秒片段，第一段作为参考 prompt，第二段作为目标延续。
- 评估协议：VPC24 与 VPC26 Track 1，指标包括 WER↓、UAR↑、EER↑，并报告 EER-L 与 EER-S。
- 内容表示线性探测：LiveAnon 的 ASR 表示较 SVA 内容表示具有更高情感 UAR（55.17 vs. 39.95），同时说话人分类准确率更低（28.75 vs. 32.50）。
- VPC24 固定目标 vctk-1fix 设置：LiveAnon 在所有指标上优于 SVA，WER 4.31 vs. 4.54，UAR 44.09 vs. 39.71，EER-L 48.75 vs. 47.19，EER-S 32.28 vs. 15.92；UAR 接近 SVA 的 emotion-prompted cremad-emo-4rnd 设置（44.59），且不使用情感特定监督。
- VPC26：LiveAnon 在四个指标上均排名第二（WER 4.30，UAR 44.09，EER-L 26.08，EER-S 17.99），说明在流式设置下仍可与离线基线竞争并保持较好的隐私-效用平衡。
- 延迟与 RTF：320 ms Zipformer chunk 下算法延迟为 500 ms，RTX 4090 上 RTF 为 0.17；160 ms chunk 配置下延迟降至 340 ms，RTF 为 0.34；内容编码器是最大延迟来源。
- 消融：capped delay 的 δ_max 控制 codebook 间依赖与生成延迟的权衡，图 2 显示 delay cap 3 是最佳操作点。

## 一句话评价
LiveAnon 通过流式 ASR 隐特征条件化与 capped RVQ 解码，在不增加情感专用监督的情况下，实现了流式说话人匿名化中更优的隐私-效用-延迟平衡。

---

## 28. KOMOS: Automatic Mean Opinion Score Estimation for Korean Speech

**作者**: Sangchun Ha, Junwon Moon, Kyuhong Shim
**链接**: [2610.15353](https://arxiv.org/abs/2610.15353)
**分类**: Speech Quality Assessment / Mean Opinion Score Prediction | **关键词**: Mean Opinion Score (MOS), Korean Speech, Speech Quality Assessment, Spontaneous Speech, Self-Supervised Speech Encoder

# KOMOS: Automatic Mean Opinion Score Estimation for Korean Speech

## 核心痛点
- 随着语音生成和实时口语对话系统发展，神经 MOS 预测器被广泛用于评估语音质量；但主观 MOS 测试成本高、耗时长。
- 现有 MOS 预测器多基于英语朗读语音（如 BVCC）训练，跨语言和说话风格泛化不一致。UTMOS v1/v2 虽被用于韩语 TTS 评估，但其对韩语语音的可靠性未充分验证。
- 作者分析发现：UTMOS v1 校准后的平均预测在人类 MOS 1.0–2.0 范围高估，在 4.0–5.0 范围低估；在相同人类 MOS 桶中，UTMOS v1 对韩语自发语音比朗读语音低 0.85–1.28 分（平均 1.05 分），Mann–Whitney U 检验显著（p<.001，Bonferroni 校正后仍显著）。
- 因此需要让 MOS 预测与韩国听众判断在说话风格和质量水平上更好对齐。

## 数据集与评级协议
- 构建 1,000 条韩语语音：420 条真实录音（42%）、310 条 TTS（31%）、270 条退化语音（27%）。包含工作室朗读、自发和噪声真实录音、商业/开源 TTS、声码器/编解码器退化语音。
- 类别：6 个通用类别（Command/Information、Free-talk、Question、Emotion、Interjection、Syntactic Complexity）和 4 个韩语特定类别（紧音化、连音、汉字词数词读法、敬语）。超过 200 个人类说话人和 TTS 音色。
- 29 名韩语母语听者通过内部网页界面进行 1–5 分总体质量评分；每条语音由 5 名不同听者评分，共 5,000 条评分。话语级 MOS 为 5 个评分的算术平均。评分者间信度 ordinal Krippendorff’s α = 0.700。
- 按话语级 MOS 分层，训练/验证/测试 = 810/90/100。主划分为 seen-system 设置。测试集中额外定义 34 条说话人不相交子集和 55 条文本不相交子集。

## 方法创新
- KOMOS：韩语 MOS 预测器，评估朗读和自发语音的整体质量。采用 UTMOS 的听者条件架构：预训练语音编码器 + 128 维听者嵌入 + 回归头。
- 比较多个预训练编码器和微调策略，根据验证 SRCC 选择最终配置。最终使用 Whisper-medium 编码器（丢弃解码器，位置嵌入表截断到 500 位置以适配 10 秒输入），16 kHz 单声道，冻结卷积前端，微调其余编码器参数。
- 听者嵌入表 31 项：29 名听者 + MEAN 和 MEDIAN 两个聚合项。训练时每条话语关联 K=7 个目标：5 个个体质量评分、均值、中位数。编码器每话语处理一次，输出复用。每个目标嵌入沿时间重复，与编码器帧拼接，经单层双向 LSTM（隐藏 256），线性投影到每帧标量分数。推理时使用 MEAN 嵌入并对有效帧平均得到话语级 MOS。
- 损失：帧级裁剪 MSE 回归损失（τ=0.25） + 话语级排序损失（基于 MEAN 嵌入平均帧分数，成对排序，δ=0.5，m=0.1，λ=0.5）。总损失 L = L_frame + λ L_rank。
- 训练：AdamW，编码器学习率 1e-5，头和嵌入 3e-4，权重衰减 0.01，batch size 32，bf16，最多 20 epochs，早停。

## 实验结果
- 测试集话语级 SRCC 0.900，LCC 0.950，优于 UTMOS v1（SRCC 0.703, LCC 0.798）和 UTMOS v2（SRCC 0.767, LCC 0.858）。
- 验证集上 Whisper-medium 全微调 SRCC 0.932, LCC 0.949；测试集 SRCC 0.900, LCC 0.950。Whisper-large-v3 测试 SRCC 0.910，Whisper-large-v2 0.909，WavLM-large 0.895 等。最终选择 Whisper-medium。
- 策略比较：full-FT 最佳，frozen-ws/frozen-last/frozen-early 较差（测试 SRCC 0.871/0.860/0.840）。
- 子集：KOMOS 在 speaker-disjoint（n=34）SRCC 0.951，text-disjoint（n=55）SRCC 0.878，均优于 UTMOS v1/v2。
- 校准后预测更接近人类 MOS 尺度，尤其高 MOS 范围；在未见 TTS 系统的诊断中，校准平均预测在十个类别上符合高质量筛选标准。
- 贡献：提出 KOMOS；构建韩语 MOS 数据集；分析现有预测器在韩语上的局限并系统比较骨干和微调策略。

## 一句话评价
KOMOS 通过韩语母语者评分数据微调 Whisper-medium 等语音编码器，并引入听者条件与排序损失，显著提升韩语朗读/自发语音的 MOS 预测与人类判断的一致性，为韩语语音质量评估提供了公开模型和数据集基准。

---

## 29. HE-NAC: High-Efficiency Neural Audio Coding via Hierarchical and Residual Multi-Band Quantization

**作者**: Darius Pétermann, Wootaek Lim, Seungkwon Beack, Minje Kim
**链接**: [2610.15243](https://arxiv.org/abs/2610.15243)
**分类**: Neural Audio Coding | **关键词**: Neural Audio Coding, Residual Vector Quantization, Multi-Band Quantization, High-Fidelity Audio Coding, Blind Upsampling

# HE-NAC 论文总结

## 核心痛点
- 神经音频编码（NAC）依赖编码器激进的时间抽取（如 Descript Audio Codec, DAC 中高达 320×），导致高频细节在瓶颈处丢失，解码器被迫执行盲上采样，重建质量下降。
- 当前最佳方法常使用对抗学习来“幻觉”缺失的高频内容，虽能获得感知上合理的重建，但不够精确，对高保真音乐应用不利，可能破坏谐波结构、音色和真实感。
- 单一潜在表示上的传统 RVQ 虽然提供可扩展量化，但在高频区域重建逐渐不精确。
- 音乐等通用音频对细微感知退化非常敏感，需要更高比特率和忠实重建。

## 方法创新
- 提出 HE-NAC，将传统残差矢量量化（RVQ）从单一潜在表示扩展为渐进式多频带量化框架，允许按照目标比特率和重建需求在不同频带独立分配量化资源，同时保持比特率可扩展性。
- 架构协调两类模块：无比特率的盲上采样用于高频重建，以及专用高频残差编码器用极少比特补偿盲上采样的不精确性。二者互补学习。
- 采用多头解码器架构，实现频带特定的重建。
- 提出多阶段训练算法，在不同子带间形成感知上有意义的熵分布：强调核心频带（≤3 kHz）的重建质量，高频分量只使用恰好足够的码率来辅助盲上采样。
- 受 SBR（spectral bandwidth replication，随 MPEG-4 HE-AAC 引入）启发，但以深度学习方式实现：核心频带投入更多比特、高频信息可从核心频带推断、高频重建需要少量编码而非仅靠生成式上采样。

## 实验结果
- 在 23 kbps 下，类似 MUSHRA 的主观听力测试达到“优秀”质量。
- 在相同或更低比特率下，HE-NAC 优于 DAC 基线（同 23 kbps）和商业 HE-AAC 实现（24 kbps）。
- 客观评估与主观测试均支持上述结论。
- 能够可靠重建核心频带（≤3 kHz）成分，同时保持整体声音保真度。

## 一句话评价
HE-NAC 通过分层多频带残差量化和“盲上采样 + 低比特率残差补偿”的协同设计，在低比特率下实现了优于 DAC 和 HE-AAC 的高保真音频编码，为音乐编码提供了一种避免对抗幻觉的实用方案。

---

## 30. Word-Aligned Prosody Reflects Speaker Differences More Than Depression or PTSD Severity

**作者**: Hsiang-Chen Yeh, Aurosweta Mahapatra, Shreeram Suresh Chandra, Ryan L. Boyd, Berrak Sisman
**链接**: [2610.15181](https://arxiv.org/abs/2610.15181)
**分类**: Clinical Speech Processing (Speech-based Depression/PTSD Assessment) | **关键词**: word-aligned prosody, measurement validation, reproducibility / generalizability theory, depression, PTSD, speaker-level aggregation

# Word-Aligned Prosody Reflects Speaker Differences More Than Depression or PTSD Severity

**作者/机构**：Hsiang-Chen Yeh、Aurosweta Mahapatra、Shreeram Suresh Chandra、Ryan L. Boyd、Berrak Sisman（Johns Hopkins University CLSP / 临床心理健康咨询；Vanderbilt University）

## 1. 核心痛点（Problem）
- 词级对齐的韵律特征（word-aligned prosody）近年在抑郁、PTSD 自动检测中被广泛使用，但这些测量的**稳定性（reproducibility）与临床相关性**从未被系统验证。
- 以往语音研究的可重复性只在**录音/会话层面**检验，词级测量是否可重复尚未确立。
- 关键隐患：一个看似与抑郁相关的声学模式，可能实际上反映的是**说话人基线嗓音、录音环境或麦克风**，从而把「病情相关信息」与「说话人身份」纠缠在一起。
- 因此需要回答：一个词级声学值中，有多少是稳定的说话人属性，有多少只是该次发音的偶发状态？

## 2. 研究问题（RQ）
- **RQ1**：说话人对特定词的个性化韵律实现是否在不同话语语境（context）间复现？把词聚合成说话人摘要（speaker summary）后是否在不同录音间保持一致？
- **RQ2**：这些说话人摘要是否与抑郁（PHQ-8）或 PTSD 严重程度（PCL）相关——包括**人际间（between-person）**与**人内（within-person）**两个层面？

## 3. 方法创新（Method）
### 3.1 理论框架
- 借用**人格心理学**的「人—情境」文献：Mischel 发现单一情境行为对另一情境的预测相关低于 0.3（"personality coefficient"，共享方差 <10%）；但跨天聚合后稳定性可达 0.8–0.9。
- 由此提出**「词即情境」vs「词即场合」两种解释**：若每个词 token 主要是「一次观测场合」，则词特异偏差难以复现、但聚合成摘要稳定；若「词」是反复出现的情境，则说话人×词的偏差应能跨语境复现。
- 采用**概化理论（Generalizability Theory）**将韵律方差分解为：说话人（S）、词（W）、说话人×词（S×W）与残差（ε）。
- 遵循 **V3 框架**：先把「可重复性」作为分析效度（analytical validation）的第一关，通过后才检验临床效度。
- 强调临床测量的时间窗：抑郁定义至少 2 周、PTSD 至少 1 个月，因此**聚合**（而非单次发音）才符合临床构念。

### 3.2 特征与提取
- 四个共享特征：**mean F0、robust F0 range (P90–P10)、energy (dB)、音节归一化 log 词时长**。
- 用 WhisperX 3.3.1 对齐 16 kHz 单声道音频；F0 仅在浊音帧上用自相关估计；能量为 20log10(word RMS)；音节来自 CMUdict；四个语料使用同一套特征代码。
- 预注册：阈值、特征顺序、拟合失败规则在任何估计被查看前固定；症状分数在对应特征通过可重复性检验前保持隐藏；事后分析均标注 post hoc。

### 3.3 判定门槛与稳健性
- **Gate E**：ESD 词偏差跨语境复现率须 > 0.70；**Gate M**：说话人摘要一致性须 > 0.60。
- 还须通过预注册的 bootstrap、留一说话人（leave-one-speaker-out）与等权（equal-weight）稳健性检验。
- 跨语境复现定义：Rc = σ²_SW,c /(σ²_SW,c + σ²_e,c)，即 S×W 交互项的单次观测组内相关（ICC）。原始 token 保留说话人层级，其信息量为 (σ²S+σ²SW)/(σ²S+σ²SW+σ²e) ≈ 0.23–0.37。

## 4. 实验设置（数据集）
| 语料 | 类型 | 规模 | 用途 |
|---|---|---|---|
| **ESD** | 表演式情感语音 | 9 位英语说话人（4 男 5 女），每人同一 350 句 × 5 种情感条件，98,202 tokens | RQ1（跨语境复现）|
| **MSP-Podcast** | 自发情感语音 | 99 位说话人（62 男 37 女），551,759 tokens，按完整 episode 划分两半 | RQ1（跨录音一致性）|
| **DAIC-WOZ** | 临床半结构化访谈 | 189 位有 PHQ-8 分数的参与者，其中 56 位带二分类抑郁标签 | RQ2 |
| **PTSD-STOP** | 每日视频日记 | 219 位世贸中心救援人员（84% 男性），13,600 段每日独白，当日 PCL 评分 | RQ2（人内/跨时间）|

## 5. 主要结果（Results）
### RQ1：词级不稳定，说话人摘要高度稳定
- **词特异偏差几乎不跨语境复现**：ESD 复现率仅 **0.01–0.16**（mean F0 = .059、F0 range = .160、energy = .029、log duration = .010），多数未通过 Gate E。
- **说话人摘要一致性极高**：
  - ESD：**0.997**（但性别与录音通道部分贡献了这个上限）；
  - MSP-Podcast：**0.73–0.90**（mean F0 .895、energy .869、log duration .793、F0 range .732）；
  - DAIC-WOZ 与 PTSD-STOP：**0.84–0.996**。
- 结论：词对齐韵律主要捕捉的是一个**可加的说话人层级（additive speaker level）**，几乎没有稳定的说话人×词结构；稳定性来自**跨词聚合**，而非单个词。

### RQ2：稳定 ≠ 有临床效度
- 与抑郁或 PTSD 严重程度的关联**不超过 0.15**；
- 等价性检验（equivalence test）在所有分析中排除了 0.30 的效应，在 DAIC-WOZ 中甚至排除了 0.20；
- 人内层面与**当日 PTSD 症状**的关联接近零（|ρ| ≤ 0.04）。
- 即使 DAIC-WOZ 正是词级抑郁分类器（本研究动机来源）的开发区，也未发现可检测的词级临床信号。

## 6. 结论与贡献
- 聚合确实能产生**稳定、可重复的说话人级韵律测量**，但在这四个语料中，这些测量**无法可检测地追踪抑郁或 PTSD 严重程度**。
- 这是**首个**评估词级韵律特征作为抑郁/PTSD 行为标记的跨语境可重复性的研究。
- 方法学启示：测量可重复性是临床效度的必要非充分条件；单一词级声学值约等于「人格系数」量级的弱证据，不宜直接当作临床证据使用。
- 代码开源：https://github.com/jen900704/word-aligned-prosody

## 7. 一句话评价
> 该论文以严谨的测量学视角「泼冷水」：词级韵律的稳定成分几乎全是说话人基线特征，聚合后虽高度可重复，却与抑郁/PTSD 严重度无实质关联——提醒社区在把词级声学特征当作临床生物标记前，必须先过可重复性这一关。

**局限提示**：ESD 为表演语音、样本仅 9 人导致 bootstrap 区间有偏（区间偏低下界）、duration 特征因音节效应被移除说话人固定效应而不可与其他三特征直接比较；MSP-Podcast 的 split-half 依赖录音通道/性别等因素。

---

## 31. SemiCodec: Bridging Speech Tokenization and High-fidelity Reconstruction with Semi-discrete Representations

**作者**: Kecan Mao, Nan Xu, Zhaoyang Meng, Zhengyao Ma, Yingming Gao, Yi Zhao, Ya Li
**链接**: [2610.14834](https://arxiv.org/abs/2610.14834)
**分类**: Neural Speech Codec | **关键词**: Semi-discrete speech representation, Neural speech codec, Speech tokenization, Preserve-then-Ground, High-fidelity reconstruction

# SemiCodec：用半离散表示打通语音 tokenization 与高保真重建

## 核心痛点
- 语音同时包含离散的语言内容与连续的声学细节（说话人、韵律、情感等）。
- 现有离散编解码器（DAC、Mimi、WavTokenizer、X-Codec、DualCodec、SAC、OmniCodec 等）提供紧凑 token，利于语言建模和下一 token 预测，但低帧率量化容易丢失细粒度声学信息。
- 连续表示（Semantic-VAE、Ming-UniAudio、dots.tts 等）避免硬量化，保真度更高，但通常需要回归、流匹配、扩散或专门的连续自回归目标。
- 因此，如何同时保留紧凑离散接口和高保真声学重建，是核心问题。

## 方法创新
- 提出 SemiCodec：一种半离散神经语音编解码器，同时输出 SSL 引导的离散 token 和连续声学隐变量，并将两个流投影到共享合成空间中相加融合后解码：x̂ = G(D_s(s) + D_a(z_a))。
- 识别出直接联合训练中的“连续路径重建捷径”：连续分支不受有限码本约束，早期收敛更快，解码器容易过度依赖连续路径，导致离散 token 没有被充分用于波形合成；仅靠 SSL 蒸馏也无法保证离散特征真正参与重建。
- 提出 Preserve-then-Ground 两阶段训练范式：
  - 阶段 I（Acoustic Detail Preservation）：禁用离散分支，先训练波形编码器、连续分支和解码器，建立稳定、高保真的声学合成空间。损失为 L_wav + λ_KL L_KL。
  - 阶段 II（Discrete Token Grounding）：冻结波形编码器和连续分支，将其作为稳定声学锚点；引入离散分支，用 L_wav + λ_SSL L_SSL + L_VQ 联合优化离散分支和波形解码器，使离散 token 进入并补充已有合成空间。
  - 声学 Dropout：阶段 II 中以概率 p 随机丢弃连续分支输出，迫使解码器在 m=0 时必须依赖离散流，从而强化离散 token 的重建贡献。
- 结构细节：共享编码器为因果卷积 + Qwen2 风格 Transformer，输出 25 Hz 帧级表示；波形解码器经转置卷积上采样后再接 Transformer，并用 iSTFT 头直接预测复数谱重建波形，无需 mel 中间表示或外部声码器。连续分支使用 64 维变分瓶颈；离散分支使用 4096 条码本、8 维嵌入和直通估计器。离散分支还通过冻结的 w2v-BERT 2.0 第 17 层特征进行 SSL 蒸馏。

## 实验结果
- 训练数据规模约 795K 小时（95K 小时 Emilia/LibriTTS + 700K 小时内部数据），采样率 24 kHz，训练片段随机裁剪至 9.6 秒，使用 32 张 NVIDIA H20 GPU、BF16 训练。
- 在 LibriSpeech test-other 上评估重建质量，指标包括 PESQ NB/WB、STOI、ViSQOL、SIM、WER 和 MUSHRA。
- 主要结果：SemiCodec（24 kHz、25 FPS）取得 PESQ NB 4.15、WB 4.03、STOI 0.975、ViSQOL 3.77、SIM 0.96、WER 5.02%、MUSHRA 86.95±1.35。相比全离散基线（WavTokenizer、X-Codec2、SAC），在 PESQ、STOI、SIM、MUSHRA 等指标上明显更优；与连续基线（Semantic-VAE、Ming-omni-tts VAE、dots.tts VAE）相比，在感知质量和可懂度上具有竞争力，例如 MUSHRA 高于 dots.tts VAE 的 82.83±1.65，但 ViSQOL 和部分声学保真度略低于 dots.tts。
- 消融研究表明：直接联合训练效果最差（PESQ NB 3.87、WB 3.58、ViSQOL 3.58、WER 5.15%）；阶段 I 已显著提升；阶段 II 进一步提升；加入 Acoustic Dropout 后达到最佳（PESQ NB 4.15、WB 4.03、ViSQOL 3.77、WER 5.02%），验证了两阶段范式和声学 Dropout 的有效性。

## 一句话评价
SemiCodec 通过“半离散表示 + 先保留后接地”的巧妙设计，在离散建模接口与高保真语音重建之间取得了更好的平衡，为语音 tokenization 与神经编解码器研究提供了有前景的新范式。

---

## 32. Cross-Lingual TTS for Indian Languages: A Benchmark and Inference-Time Duration Estimation Strategies

**作者**: Adarsh Arigala, Arjun Gangwar, Srinivasan Umesh
**链接**: [2610.14826](https://arxiv.org/abs/2610.14826)
**分类**: Text-to-Speech | **关键词**: Cross-Lingual TTS, Alignment-Free TTS, Duration Estimation, Indian Languages, Speech Synthesis Benchmark

## 论文总结：Cross-Lingual TTS for Indian Languages

### 核心痛点（Problem）
- **无对齐（alignment-free）TTS 模型在跨语言场景下性能退化**：E2-TTS、F5-TTS、A-DMA 等模型通过移除显式对齐模块简化训练并在同语言合成中取得高质量，但当参考语音与目标文本语言不一致时，因书写系统、正字法特征与**语言相关的每字符时长（duration-per-character）差异**，会出现严重的时长失配（duration mismatch），导致语音质量下降。
- **F5-TTS 的时长估计基于 UTF-8 字节数而非字符数**：不同书写系统的字符占用的 UTF-8 字节数不同（印度语言字符通常占多字节，英文通常 1 字节），且各语言每字符时长模式不同，导致估计时长不准确。
- **现有解决方案需增加模型复杂度**：如 Cross-Lingual F5-TTS 需 MMS 强制对齐预处理与单独训练的语速预测器；PFluxTTS 依赖显式时长预测器，重新引入了时长建模，削弱了无对齐 TTS 的优势。
- **印度语言跨语言 TTS 缺乏标准化评测基准**：印度人多语混用（英语+地区语言）场景重要，但系统性评估欠缺。

### 方法创新（Method）
1. **构建跨语言评测基准**：覆盖英语 + 九种印度语言（卡纳达、泰卢固、泰米尔、印地、马拉雅拉姆、旁遮普、孟加拉、奥里亚、马拉地），每种语言约 2 小时评测数据（约 1 小时英语参考+印度语生成，1 小时印度语参考+英语生成），数据取自 Rasa、IndicVoices-R 测试集与 IndicTTS 训练集，参考语音时长约束 4–7s、目标 4–10s。共约 1000+ 句/语言对。
2. **基线模型**：采用 A-DMA（基于 F5-TTS 骨干），结合条件流匹配（CFM）损失 + 文本级（CTC on intermediate layer）与语音级（data2vec-AQC 第 21 层 SSL 表示）对齐损失，L = L_CFM + 0.1·L_text + 1.0·L_speech。
3. **从头训练双语言与多语言 A-DMA 模型**：
   - 双语言：F5-TTS Small（18 层 DiT、12 头、768 维 Embedding + 4 层 ConvNeXtV2、512 维），159M 参数，每种印度语 + 30 小时印度英语，训练 1.2M 步。
   - 多语言：F5-TTS Base（22 层 DiT、16 头、1024 维 + 4 层 ConvNeXtV2、512 维），335.8M 参数，24 种语言，300k updates。
   - 24kHz 采样、100 通道 mel、hop 256，Vocos 声码器，AdamW，峰值学习率 7.5e-5。
4. **语言感知的推理时时长估计策略（无需重训、无架构改动）**：
   - **Modified F5-TTS**：将原始 F5-TTS 的 UTF-8 字节时长公式改写为字符级空间。原始公式：D_F5 = D_ref + ⌊(D_ref/L_ref)·L_gen/s⌋。
   - **Heuristic-1 (H1)**：融合式，D_H1 = D_ref + α⌊(D_ref/L_ref)·L_gen/s⌋ + β(D_ind + D_eng)，α=0.7、β=0.3；其中 D_ind = dc_ind×C_ind、D_eng = dc_eng×C_eng。
   - **Heuristic-2 (H2)**：加性交互式（additive interaction）时长建模。
   - 每字符时长统计：dc = L_audio / C_text = (N_samples/H)/C_text，按语言在训练语料（共 3248.5 小时，覆盖 24 语言）上跨全部说话人平均得到 dc_lang。

### 实验结果（Results）
- 在双语言与多语言 A-DMA 模型上，所提语言感知推理时时长估计策略**提升了语音自然度、可懂度与说话人相似度，同时降低了时长失配**。
- 相较需要重训的显式时长预测器方案，本方法零重训、零架构改动，直接在推理阶段融合语言相关每字符时长统计。
- 论文构建的基准可系统分析两种跨语言设定（英→印、印→英）下的 TTS 表现，填补了印度语言跨语言评测空白。

### 一句话评价
该工作以极低工程代价（纯推理时、无需重训与改架构）解决了无对齐 TTS 跨语言时长失配问题，并首次为英语—九种印度语言的跨语言 TTS 提供了标准化评测基准，兼具实用性与评测价值。

---

## 33. FAM-gate: field-aware metadata attention with prior-constrained vector gating for audio classification

**作者**: Xiangyu Jing, Hongqing Liu, Liming Shi
**链接**: [2610.14673](https://arxiv.org/abs/2610.14673)
**分类**: Audio Classification | **关键词**: Audio Classification, Metadata Fusion, Field-Aware Attention, Prior-Constrained Vector Gating, Audio-Language Models, Multimodal Learning

## 核心痛点
- 用户生成音频常伴随标题、标签、描述等文本元数据，但已有 audio-only 模型在声学相似但语义不同、类内方差大的场景中表现受限。
- 类别级文本（如 CLAP 的类名文本）缺少录音级上下文；样本级元数据可补足这一缺口，但字段高度异质：结构、语义密度和噪声水平各不相同。
- 现有简单拼接或随机选择字段的方法忽略录音依赖的字段相关性；标量门控对所有特征维度施加统一融合权重，无法建模通道级跨模态互补与冲突。
- 通用多模态特征重校准方法如 MMTM、FiLM 未显式处理元数据字段噪声，也未将融合约束在声学先验附近。

## 方法创新
- 提出 FAM-Gate 两阶段框架，基于预训练 LAION-CLAP（HTSAT 音频编码器 + 共享 RoBERTa 文本编码器），并用字段掩码处理缺失元数据字段。
- 第一阶段 Field-Aware Metadata View Attention (MVA)：以音频 embedding 作为 query 引导字段选择；采用共享残差投影 S(z)=z+Wz 与 ℓ2 归一化，尽量保持预训练 CLAP 空间几何；引入字段身份嵌入 p_v 保留字段身份；通过缩放余弦相似度、数据集级字段先验 c_v 和掩码 softmax 得到字段权重 α_v；保留原始文本 embedding 作为 value，并以掩码均值 e_mean 为锚，用 γ=tanh(ρ) 进行有界偏离聚合 e_m=e_mean+γ(e_att−e_mean)，当 γ=0 时可退化为掩码均值基线。
- 第二阶段 Prior-Constrained Vector Gate (PCVG)：输入音频特征 h_a 与聚合元数据特征 h_m，构造交互表示 r=[h_a;h_m;h_a⊙h_m;|h_a−h_m|]，经 LayerNorm、两层 MLP 和 tanh 得到有界残差 δ；门控 g=σ(β+ηδ)，其中 β 为可学习声学先验向量，η 控制更新最大动态范围；最后按维度插值 h_f=Dropout(LN(g⊙h_a+(1_D−g)⊙h_m))，大 g 偏向声学证据，小 g 偏向语义元数据。
- 预测与目标：单标签设置使用标准交叉熵，多标签设置使用带 logits 的二元交叉熵。
- 主要贡献：对齐保持、字段感知、均值锚定的异质元数据聚合机制；先验约束向量门控以建模维度级跨模态互补与冲突；在 BSD10K、BSD35K、FSD50K 上五种子匹配评估显示一致增益，且总参数仅增加 0.19%。

## 实验结果
- 数据集：BSD10K（23 个单标签叶类）、BSD35K（28 个单标签叶类），使用固定 90/10 样本级划分（seed 3407），报告 leaf accuracy 与 weighted hierarchical F-score（λ=0.75）。FSD50K 含 200 个多标签声音类，采用官方 train/validation/evaluation 划分，报告 macro mAP 与阈值 0.5 下的 macro F1。
- 主要提升：与匹配的 random-view scalar-fusion 基线相比，FAM-Gate 在 BSD10K 和 BSD35K 上分别将 hierarchical F-score 提升 2.53 和 5.72 个百分点；在 FSD50K 上将 macro mAP 和 macro F1 分别提升 5.07 和 10.25 个百分点。
- FSD50K 官方评估：FAM-Gate 取得 74.98±0.23 mAP，输入为 Audio+Metadata，优于 PaSST-S 的 65.30、TFECN 的 67.29、MN (α=3.0) 的 65.60、DyMN-L 的 65.50。
- 消融：比较六种匹配变体，包括 Random View + Scalar、PCVG Only、Mean + PCVG、Projected MVA + Scalar、Projected MVA + PCVG、FAM-Gate；所有变体共享 LAION-CLAP 骨干、预测头、数据划分和训练超参；每个配置用五个固定随机种子评估，报告 mean±sample std；每次运行在单张 NVIDIA RTX A6000 GPU 上训练。
- 效率：相比基线，总参数量仅增加 0.19%。

## 一句话评价
FAM-Gate 通过字段感知元数据注意力和先验约束向量门控，在保持 CLAP 音文对齐的同时实现参数高效、维度级的音频-元数据融合，并在 BSD10K、BSD35K 与 FSD50K 上取得一致提升，但其在更广泛领域和元数据缺失/噪声场景下的鲁棒性仍需进一步验证。

---

## 34. RUBATO: Decoupled Clocks Allow Full-Duplex Models to Think as Fast as They Can

**作者**: Yi-Jen Shih, Puyuan Peng, Haohe Liu, David Harwath, Abdelrahman Mohamed
**链接**: [2610.14299](https://arxiv.org/abs/2610.14299)
**分类**: Error | **关键词**: 

总结生成失败: Extra data: line 2 column 1 (char 24)

---

## 35. GeoMER: A Joint Euclidean-Hyperbolic Geometry Framework for Multimodal Emotion Recognition

**作者**: Ting Zhu, Huizhi Liang, Boguslaw Obara, Shufei Duan, Varun Ojha
**链接**: [2610.18587](https://arxiv.org/abs/2610.18587)
**分类**: Multimodal Emotion Recognition (Speech-Text) | **关键词**: Multimodal Emotion Recognition, Hyperbolic Geometry, Speech Emotion Recognition, Multimodal Feature Fusion, Affective Computing

## 核心痛点
- 多模态情感识别（MER）需要融合语音、文本等模态理解情感，但现有方法多依赖欧氏空间表示，擅长细粒度跨模态交互，却缺乏组织情感层级/抽象结构的几何先验。
- 心理学研究表明情感语义存在潜在层级结构化关系（如情绪混合、强度变化：annoyance→anger→rage），而标准欧氏隐空间不显式建模这种结构。
- 已有双曲方法多集中于标签层级、嵌入或通用欧氏/双曲层组合，混合几何方法通常耦合松散，缺少统一联合优化框架来同时保留欧氏判别性跨模态对齐与双曲层级结构建模优势。

## 方法创新
- 提出 GeoMER：面向 MER 的欧氏-双曲联合建模框架，包含欧氏分支和双曲分支，通过统一融合机制联合优化。
- EuclFusion（Euclidean Multimodal Fusion Module）：在欧氏空间进行跨模态交互建模，沿用 MemoCMT 架构并改进，加入双向 LSTM（BiLSTM）对融合后的多模态 token 序列进行时序聚合，先生成固定长度 utterance-level 表示 h_euc。
- HypGeoRoute（Hyperbolic Geometric Core Routing）：将多模态 token 表示投影到 Poincaré ball，通过几何感知路由和 core-wise aggregation 捕获更抽象的情感结构表示。
- 特征对齐：使用轻量欧氏 adaptor（Linear + LayerNorm + Dropout）对齐音频和文本嵌入，再通过指数映射 exp_0 投影到双曲空间。
- 几何核心路由：引入 N_c 个可学习几何核心 {μ_k}，基于 Poincaré ball 中的双曲距离 d_mik 计算 token 到核心的路由权重 α_mik，采用 soft routing 允许 token 被分配到多个核心，建模情感混合。
- 核心聚合：使用 Einstein midpoint 思想，通过 log_0 映射到原点切空间进行路由加权聚合，再用 exp_0 映射回双曲流形，得到各模态各核心的抽象情感原型表示。
- 贡献还包括 core-wise hyperbolic self-attention，用于在 Poincaré ball 中捕获几何核心间关系，保持几何一致性并增强上下文建模。
- 最终将双曲表示映射回欧氏空间，与欧氏特征拼接后用于情感分类，兼顾判别性语义与抽象层级结构。

## 实验结果
- 在 IEMOCAP 多模态 MER 基准上实验。
- 取得最佳性能：加权准确率 83.54%，非加权准确率 83.35%。
- 优于欧氏基线，包括 MemoCMT。

## 一句话评价
GeoMER 通过欧氏-双曲双几何联合框架，在保留跨模态细粒度对齐的同时引入双曲几何先验建模情感层级/混合结构，在 IEMOCAP 上取得优于欧氏基线的 MER 性能，体现了非欧表示在情感计算中的互补价值。

---

## 36. SonicWorld: Source-Centric Latent Dynamics for Spatial Audio Reasoning

**作者**: Chenlong Wei, Hanling Wang, Mingjin Lou, Yufan Shi, Yandong Sun, Sheldon Yu, Xiaohui Zhu, Xiaobo Jin, Yiwei Wang
**链接**: [2610.17131](https://arxiv.org/abs/2610.17131)
**分类**: Spatial Audio Reasoning / Audio-Language Models | **关键词**: Spatial Audio Reasoning, First-Order Ambisonics (FOA), Source-Centric State Inference, Latent Dynamics, Omni LLM, Sonic-Bench

# SonicWorld: Source-Centric Latent Dynamics for Spatial Audio Reasoning

## 核心痛点
动态空间音频推理要求模型将不断变化的声学观测与正确的声源关联起来，并在查询的时间点或时间区间内恢复该声源的空间状态。这一任务在**重叠语音**和**声源运动**的场景下尤为困难。现有方法（如双耳特征、FOA 强度矢量、并行空间分支）虽然让语言模型能够接触到空间线索，但大多是**逐帧（frame-wise）或源无关（source-agnostic）**的，无法在重叠与运动条件下维持稳定的声源身份（source identity），因此难以回答"某一特定声源在某时刻在哪里/如何运动"这类问题。

## 方法创新
### 1. Sonic-Bench 基准
- 包含 **2.8K 一阶 Ambisonics（FOA）音频片段**、**28.8K 目标特定问答对**，覆盖 **480 个仿真室内场景**。
- 覆盖单源与双源设置下的**定位、距离估计、运动推理**。
- 采用场景不相交（scene-disjoint）的训练/测试划分（2400 训练片段/400 场景，480 测试片段/80 场景）。
- 查询类型包括：位置方向（8 扇区）、方位角、仰角、距离、运动方向（8 方向或 Stationary）。
- 数据基于 HM3D 场景网格、Habitat-Sim 渲染，语音来自 Mini LibriSpeech，双源片段配对一男一女声音。

### 2. SonicWorld 框架
- 将**物理特征、学习到的声学特征、语义特征**整合为**持久化声源状态（persistent source states）**，通过**学习到的状态转移**与**循环观测更新（BiGRU）**建模其时间演化。
- **物理分支**：通道对数幅度 + 有源/无源强度（intensity）+ 通道间相干性，经 2D CNN 生成物理 token。
- **神经分支**：仿 Neural IV，将 W 通道与 X/Y/Z 的逐元素交互拼接后映射为神经网络 token。
- **语义分支**：冻结的 BEATs 提取 patch，通过注意力池化为语义 token。
- **训练信号**：轨迹监督 + 掩码状态预测（随机掩码时序特征跨度，从上下文恢复源几何），将状态锚定在声源几何上。
- **空间投影器**将状态序列转为 token，与音频 token、问题 token 一起输入 Omni LLM。
- **两阶段微调**：Stage I 投影器对齐，Stage II LoRA 适配，两阶段均使用 L_QA + λP·L_align。

## 实验结果
- 在 Sonic-Bench 测试集上对比 **Spatial-Omni**：方向准确率从 **31.98% → 34.69%**，方位角误差从 **57.22° → 48.01°**。
- 零样本迁移到 **Spatial LibriSpeech**：方向准确率 **73.98%**、方位角误差 **19.29°**，而 Spatial-Omni 仅为 **27.14%** 和 **70.74°**，提升显著。
- 在三种语言骨干模型上均取得一致的方向与方位角增益。

## 一句话评价
SonicWorld 将动态空间音频推理重新表述为"以声源为中心的状态推断"问题，通过持久化声源状态与循环潜在动力学建模，在重叠与运动场景下显著优于现有源无关方法，并配套发布了具有挑战性的 Sonic-Bench 基准。

---

## 37. D2: High-Capability Full-Duplex Spoken Language Models from Half-Duplex Backbones

**作者**: Cheng-Kuang Chang, Alexander H. Liu, Brian Kingsbury, Hilde Kuehne, Rogerio Feris, Samuel Thomas, James Glass, Kai-Wei Chang
**链接**: [2610.17124](https://arxiv.org/abs/2610.17124)
**分类**: Full-Duplex Spoken Language Models | **关键词**: Full-Duplex Spoken Language Models, HD-to-FD Conversion, Streaming Encoder Distillation, Supervised Fine-Tuning, Chunk-Size Trade-offs, VoiceBench

# D2: High-Capability Full-Duplex Spoken Language Models from Half-Duplex Backbones

## 核心痛点
- 全双工语音语言模型（FD-SLMs）支持同时听与说、打断和重叠语音，但通用能力通常落后于强半双工语音语言模型（HD-SLMs），如音频理解、知识、推理和指令遵循。
- 已有 HD-to-FD 转换方法如 BayLing-Duplex 受限于音频编码器块长（最高 4 秒）和 800 ms chunk，延迟较高；提高更新率会导致生成不稳定和明显性能退化。MiniCPM-o 4.5 在 1 秒 chunk 下有效，但降到 0.1 秒时退化严重。
- 因此需要一种方法，将强半双工骨干转换为高能力、细粒度、低延迟的全双工模型，同时避免高更新率下的能力损失。

## 方法创新
- 提出 Dialogue-to-Duplex（D2）框架，将预训练 HD-SLMs 转换为 FD-SLMs，把全双工交互视为更细时间粒度上的普通对话。
- 形式化：HD 按完整用户轮次建模；FD 按 chunk 时长 kΔ 建模，其中 k 为每个 chunk 的编码器帧数，Δ 为编码器帧分辨率。k 越小，模型观察和响应用户越频繁，交互越细。
- Stage I 流式编码器蒸馏：将原离线或块流式音频编码器转换为流式学生编码器，使用 block-causal attention，即 chunk 内双向、跨 chunk 因果；从未改变的离线教师编码器蒸馏帧级表示。该方法不需要原始训练解码器或转录标签。
- Stage II D2 监督微调：将普通轮次对话放到共享时间线，保留静默和重叠语音，并切分为 kΔ chunk。每个 chunk 输入当前用户音频与前一个模型输出音频，自回归生成 k 个输出帧。使用教师强制训练，显式控制 token 表示响应启动和打断，padding token 占据无词汇输出位置；损失中对稀疏控制事件上加权，对 padding 下加权。
- 推理阶段逐 chunk 处理新累积用户音频和延迟自音频反馈，持续捕获用户音频，即使模型正在说话；每个 chunk 生成 k 个输出帧。
- 系统研究 chunk size 对全双工交互、通用能力和推理计算的影响。

## 实验结果
- D2 应用于两个 HD-SLM 架构：Qwen3-Omni 和 LLaMA-Omni 2。
- 在 12.5 Hz 更新率（80 ms chunk）下，Qwen3-Omni-D2 达到：99.2% turn-taking success，521 ms 延迟；99.5% interruption success；VoiceBench 得分 70.1，为评估的 FD-SLMs 中 SOTA。
- Qwen3-Omni-D2 超过最强评估全双工基线 9.1 分，并在 Full-Duplex-Bench 上验证交互能力。
- 训练数据方面，Stage I 编码器蒸馏使用 LibriSpeech train-clean-100/360 和 AVQA 音频；Stage II 从 InstructS2S-200K 与 SODA 的轮次对话构建全双工训练序列，并加入 AVQA 保持通用音频理解，模型响应用 Kokoro TTS 重合成以提供一致输出声音。

## 一句话评价
D2 通过流式编码器表示蒸馏和细粒度全双工监督微调，把强半双工语音语言模型高效转换为高能力全双工模型，在高更新率下同时保持优秀交互性与通用能力，为 FD-SLM 提供了可扩展的转换范式。

---

## 38. PitchIn: Natural-Language Vocal Coaching from Unstructured Community Feedback

**作者**: Hayeon Bang, Hounsu Kim, Joonyong Park, Jung-Jae Yu, Juhan Nam
**链接**: [2610.17036](https://arxiv.org/abs/2610.17036)
**分类**: Audio-Language Models for Vocal Coaching / Music Education | **关键词**: vocal coaching, audio-language models, instruction tuning, community feedback, singing assessment, PeerCoach Dataset

# PitchIn 论文总结

## 核心痛点
- 有效的声乐指导需要把演唱中的问题与纠正建议对应起来，但带有专家诊断和建议的录音数据非常稀缺。
- 在线歌唱社区中存在大量演唱录音与听众反馈，但观察和建议分散在非结构化评论中，难以直接作为监督信号。
- 现有自动歌唱评估多聚焦于质量打分或排序，缺少面向自然语言诊断与纠正建议的 coaching 能力。

## 方法创新
- 提出 PitchIn：面向自然语言声乐指导的音频-语言模型，并构建 PeerCoach Dataset。
- PeerCoach Dataset 包含 14,445 条指令示例，覆盖三类目标：
  - Focused QA (FQA)：把具体观察和建议转化为问答对。
  - Overall Feedback (OF)：把分散在评论线程中的反馈整合为对整体反馈请求的连贯回答。
  - Recognition QA (RQ)：辅助多选题监督，包括 Real-Feedback MCQ 与 Synthetic-Defect MCQ。
- 数据来自 Reddit 的 r/singing 与 r/ratemysinging 社区，时间跨度 40 个月；原始语料包含 9,753 条演唱录音、75,684 条评论、158.1 小时音频，并用 Mel-Band RoFormer 提取人声。
- 微调策略：在 Qwen2.5-Omni-7B 上训练 FQA+OF 得到 PitchIn-Q；在 MOSS-Music-8B-Instruct 上训练 FQA+OF 得到 PitchIn-M。采用 rank-64 LoRA，冻结包括音频编码器在内的预训练参数。
- 设置 Raw Comments 对照，直接使用源评论训练，以验证结构化 coaching target 的收益。

## 实验与结果
- 在 VocalCoachBench (VCB) 上评估，该基准包含 515 条演唱录音和 1,064 条专家评审。
- 请求的诊断-纠正对中，匹配专家问题且建议有效的比例：
  - Qwen2.5-Omni：从 21.3% 提升到 61.0%。
  - MOSS-Music：从 31.4% 提升到 51.2%。
  - 直接训练源评论的 Qwen2.5-Omni 仅有 19.8%。
- 对 Qwen 而言，仅 FQA 可达到 65.6%，但加入 Overall Feedback 后更符合专家评审与人类偏好。
- 两个模型均比预训练基线更好地对齐专家评审；有用性人类偏好分别为 92.0% 和 67.3%。
- 消融显示：结构化 OF 监督优于直接训练源评论；FQA、OF、RQ 的组合对自由式 coaching 与结构化歌唱评估有不同影响。

## 一句话评价
PitchIn 通过将非结构化社区反馈转化为结构化声乐指导监督，显著提升音频-语言模型的诊断与纠正建议生成能力，为音乐教育等专业领域的反馈生成提供了可扩展范式。

---

## 39. Deep Speech Representations Track Word Timing along a Low-Dimensional Circular Trajectory

**作者**: Burin Naowarat, Hao Tang, Sharon Goldwater
**链接**: [2610.16273](https://arxiv.org/abs/2610.16273)
**分类**: Speech Representation Learning | **关键词**: speech representation geometry, word timing, word segmentation, self-supervised speech models, HuBERT, circular trajectory, interpretability

# Deep Speech Representations Track Word Timing along a Low-Dimensional Circular Trajectory

**作者**: Burin Naowarat, Hao Tang, Sharon Goldwater (爱丁堡大学语音技术研究中心)

## 核心痛点
语音时序（speech timing）是语音模型准确识别单词的基础，但**深度语音模型如何在表征空间中编码词内时序信息**这一问题长期被忽视。以往工作多关注探测式（probing）分析（即信息是否可访问），却很少揭示信息在表征中的**结构组织方式**。认知神经科学中的几何分析方法（将神经激活视为高维时序向量，寻找与任务相关的低维子空间）为回答该问题提供了新视角，但在语音技术领域应用尚少。

## 方法创新
1. **问题一：旋转动力学的普遍性**——沿用 Zhang et al. [16] 的发现（HuBERT 特征按词时长分组平均后，在二维「时间子空间」中从词起点到词终点形成近圆形轨迹），本文在 **10 个深度语音模型**上系统验证该现象是否普遍存在。
2. **时间子空间估计**：使用 **CPCA（Centroid-PCA）**——先按词时长分组并对齐帧做平均以消除非时序因素，再对所有质心做 PCA，取前两个主成分（占总方差 54%–79%）作为时间子空间。
3. **圆轨迹的量化指标**：
   - **R²**：旋转角度与词内已历时比例之间的线性关系强度（恒定角速度）；
   - **completion%**：词终点时完成的旋转百分比（理想为接近 100%）。
4. **问题二：个体词级别可用性 → RoSeg（Rotary Segmentation）**——一种全新的词分割算法，将语音表征投影到二维时间子空间，每当完成一次完整旋转即预测一个词边界。探索了两种时间子空间估计方法，其中较优方法显著提升性能。

## 实验结果
- **普遍性验证**：圆形轨迹在架构与训练目标各异的模型中广泛出现，包括自监督（HuBERT、MelHuBERT、Wav2Vec2、WavLM、DinoSR、SpidR）与监督（Whisper encoder、VibeVoice）模型，涵盖因果/非因果架构与多种位置编码。HuBERT 中角度与词内比例的相关性 **R² = 0.983**。
- **负面对照**：在未训练的 Whisper 编码器和 log Mel 特征中**未发现**该模式；未训练的 HuBERT 中仅出现较弱的同类模式。
- **词分割（LibriSpeech test-clean）**：RoSeg 达到 **64.3% 边界 F-score** 与 **39.8% token F-score**，在多音节词上仅有适度退化。
- **对比基线**：此前最优的基于相邻帧不相似度峰值的方法仅达到 43.9% 边界 F-score 和 16.9% token F-score，说明 RoSeg 大幅提升。

## 实验设置
- 数据集：LibriSpeech dev-clean（子空间估计）、test-clean（分割评测）；词边界来自 Kaldi 强制对齐，仅保留时长 100–700 ms 的词段。
- 帧率：多数模型 50 Hz；Mimi 使用 25 Hz 连续特征，VibeVoice 使用第 5 层（60 Hz）。

## 一句话评价
本文以表征几何为工具，证明了「单词时序沿低维圆形轨迹编码」是深度语音表征的**普适性质**，并提出 RoSeg 首次将这一旋转动力学用于个体词级分割，揭示出自监督 HuBERT 蕴含远超以往认知的隐式词形知识。

## 局限与展望
- CPCA 与 RoSeg 的子空间估计均为**监督式**（需要词边界知识）；
- 圆形与某些螺旋（恒定角速度、每词一圈）在度量上尚不可区分，留待未来工作；
- 仅使用前两个 PCA 主成分，其余维度未探索。

---

## 40. BridgeCodec: Mamba Enhanced Neural Audio Codec with Schrödinger Bridge at Low Bitrate

**作者**: Zijian Lin, Jing Yang, Jinghao Luo, Zhuo Wang, Fan Fan, Zhiyong Wu
**链接**: [2610.15453](https://arxiv.org/abs/2610.15453)
**分类**: Neural Audio Codec | **关键词**: Neural Audio Codec, Schrödinger Bridge, Mamba, Low Bitrate, Latent Translation, Interoperability

# BridgeCodec: Mamba Enhanced Neural Audio Codec with Schrödinger Bridge at Low Bitrate

## 核心痛点
- 当前神经音频编解码器（NAC）通常是闭环生态，编码器-解码器严格联合训练，导致异构编解码器之间无法互通，形成“Interoperability Gap”。
- 实际部署中，设备硬件能力、计算约束不同，编解码器版本/结构冻结，无法同时更新两端，直接通信断裂。
- 现有扩散/流匹配方法通常要求预定义噪声先验（如高斯噪声），会破坏源latent中保留的语音结构先验，不适合直接桥接高度压缩的异构latent空间。
- U-Net等卷积结构感受野有限，难以建模长时语音依赖；Transformer计算复杂度二次增长。

## 方法创新
1. **BridgeCodec 框架**：将源编码器 En_s 和目标解码器 De_t 完全解耦，通过 Schrödinger Bridge（SB）在 latent 空间直接翻译源量化特征 H_s^q 到目标量化特征 H_t^q。部署时冻结源编码器、SB翻译器和目标解码器，形成灵活的非对称通信管线。
2. **Schrödinger Bridge 最优传输**：将跨编解码器latent翻译建模为SB问题，在经验分布之间自适应学习最优传输路径，无需预定义噪声先验，可对齐结构/维度/量化方式不同的压缩latent空间，并完成latent域带宽扩展。
3. **Mamba增强U-Net骨干**：在U-Net的K个分辨率层级中交错插入Mamba模块，用选择性状态空间模型以线性复杂度捕获全局时序依赖，兼顾U-Net局部特征提取和Mamba长程建模，避免卷积局部感受野限制和Transformer二次复杂度。
4. **两阶段训练策略**：
   - 第一阶段：仅在压缩latent域用bridge loss训练SB翻译器，建立异构编解码器间的鲁棒传输路径。
   - 第二阶段：将预训练SB翻译器与冻结目标解码器级联，使用联合损失 L_total = λ_bridge L_bridge + λ_t L_time + λ_mel L_mel 进行微调，其中L_time为时域L1，L_mel为梅尔谱L1，从而兼顾latent结构准确性和音频感知质量。

## 实验设置与结果
- **数据集**：ICASSP 2022 DNS Challenge 干净语音数据集，48 kHz fullband，约2,425小时、约109万条、6种语言；10,000条验证、10,000条测试，其余训练。
- **编解码器配置**：源编解码器8 kHz，ratios [2,4,5,8]，128维latent@25 Hz，4层RVQ，每层1024码本，1 kbps，2.8 MB参数；目标编解码器48 kHz，ratios [2,4,5,6,8]，128维latent@25 Hz，24层RVQ，每层1024码本，6 kbps，134 MB参数。均用开源AudioCraft训练。
- **BridgeCodec SB模型**：U-Net骨干，4个分辨率层级，每级2倍下采样（后文截断）。
- **验证场景**：将轻量8 kHz源编码器直接映射到48 kHz目标解码器，超低码率1 kbps，模拟极端非对称部署。
- **结果**：BridgeCodec实现更优的宽带重建和较高感知质量，成功桥接严重瓶颈化、异构的编解码器；即使在单函数评估（1 NFE）下仍保持高感知质量，验证了SB传输路径的结构直接性与框架鲁棒性。

## 一句话评价
BridgeCodec 用 Schrödinger Bridge 在 latent 空间打通冻结异构编解码器，并用 Mamba 增强 U-Net 捕获长时依赖，在 1 kbps 下把 8 kHz 源编码器直接桥接到 48 kHz 目标解码器，为神经音频编解码器的互操作性提供了颇具潜力的新范式。

---

## 41. JSIR: An Audio-Aligned, Multi-Task Dataset of Jazz Standard Recordings

**作者**: Sihun Lee, Dasaem Jeong
**链接**: [2610.15356](https://arxiv.org/abs/2610.15356)
**分类**: Music Information Retrieval (MIR) | **关键词**: JSIR, Jazz Standards, Music Information Retrieval, Beat Tracking, Chord Estimation, Music Structure Analysis, Multi-Task Dataset, Audio-Aligned Annotations

## 核心痛点
MIR 中的节拍跟踪、和弦估计和音乐结构分析长期由西方流行音乐数据集驱动，现有 SOTA 系统在爵士上表现显著下降：节拍跟踪器在 RWC-Jazz 上相对 RWC-Popular 损失超过 12 个百分点 F-measure，流行音乐训练的和弦识别器在五类和弦爵士词汇上仅约 40% 准确率，SALAMI 训练的边界检测器在爵士上 F-measure 减半。原因包括：爵士 swing 节奏把脉冲放在 ride cymbal 与 walking bass 而非 kick/snare，速度灵活，独奏自由跨越节拍；和声以七和弦及扩展音为主，comping 稀疏且切分，和弦起点不明确；曲式 head–solo–head 中每段 chorus 重复同一和声，重复线索不提供边界信息，段落变化更多由独奏者与乐器变化界定。已有爵士资源也有限：WJD 是独奏符号转写且仅片段，JSD 仅结构标注，JAAH 是最接近的前作但多数标准曲只有一个录音。

## 方法创新
提出 JSIR（Jazz Standards dataset for Information Retrieval）：包含 267 个商业发行录音、44 首爵士标准曲、约 25.6 小时音频（引言亦称约 29 小时），音频时长约为 JAAH 的 3.7 倍。数据集遵循两个原则：1）多任务：beat/downbeat、chord、section 三层标注共享同一 beat grid，每个和弦与段落边界都落在节拍上；2）多版本：每首标准曲有 4–9 个录音版本，支持跨版本分析。所有标注由作者（爵士音乐家）用专用工具制作，并经多轮修订。构建流程包括：从 canonical lead sheet 以 Harte 语法编码每拍一个和弦槽；用 madmom 节拍跟踪器生成初始 beat 后人工修正 octave、phase、rubato/drum solo 等漂移；手标 downbeat 并处理 irregular bars；和弦从 lead sheet 初始化后根据音频修正替换和弦、插入 no-chord N、添加新段落；结构使用六标签 intro/head/solo/trade/interlude/outro 并附加乐器标签。发布内容含 beats、chords、structure、segments 四类纯文本标注、元数据、标注工具和同步显示音频的 web 应用；因版权不发布音频，而提供 MusicBrainz 与 YouTube 标识。

## 实验结果
以近期公开模型建立三层 baseline：Beat This! 用于 beat/downbeat，Consonance-ACE 用于和弦估计，SongFormer 用于结构分析；保持架构与训练配方不变，只改变数据。由于同一标准曲的不同录音共享曲式与和声变化，所有 split 按整首标准曲分组，避免同一曲目同时出现在训练和测试中。Beat This! 采用八折交叉验证，对比仅用原 16 个数据集训练与加入 JSIR 可靠片段（340 段，20.6 小时）训练：加入 JSIR 后 beat F-measure 基本不变，但 downbeat F-measure 从 87.7% 提升到 89.2%；流行音乐训练的和弦估计器在 JAAH 上的第七和弦准确率从 34% 提升到 41%。片段在结构分析结果处截断。

## 一句话评价
JSIR 是一个面向爵士标准曲的音频对齐、多任务、多版本 MIR 数据集，显著扩展了爵士音频规模，并通过基线实验证明其能提升跨数据集的 downbeat 与爵士和弦估计表现，为爵士场景下的节拍、和声与结构分析提供了重要基准。

---

## 42. CIViC: Evidence Gates for Audio-Conditioned Visual Prediction on Proxy Tasks

**作者**: Mengzhe Geng, Max W. Y. Lam, Yuewen Cao, Shoukang Hu, Jing Xu, Marc Tessier, Xu Li
**链接**: [2610.15327](https://arxiv.org/abs/2610.15327)
**分类**: Audio-Conditioned Visual Prediction Evaluation | **关键词**: CIViC, evidence gates, audio-conditioned visual prediction, evaluation protocol, face raster, SpeakerVid, proxy tasks

# CIViC: Evidence Gates for Audio-Conditioned Visual Prediction on Proxy Tasks

**作者/机构**: Mengzhe Geng, Max W. Y. Lam, Yuewen Cao, Shoukang Hu, Jing Xu, Marc Tessier, Xu Li; NRC Canada, CUHK, Microsoft Research Asia。

## 核心痛点
音频条件视频/虚拟人生成模型常通过移除或扰动音频路径来检验输出是否变化。但仅观察到输出变化，并不能说明模型真正使用了预期的音频信息：模型可能对音频移除有反应却忽略替换音频的身份；辅助条件可能改变预测但损害留出任务；代理任务上的排序可能看似有利，而仅条件比较器反而比音频模型更好。因此，需要一个更严格的诊断协议，把条件性解释与匹配干预、留出任务比较、端点控制对应起来。

## 方法创新
论文提出 CIViC（Conditional Input and Visual Interpretation Checks），一个四门控诊断框架。它不是视频生成器，而是可证伪的“解释到控制”映射。四个门控为：
1. **Activation（激活）**: 注册移除后输出是否变化；只能排除完全不用该输入，不能说明使用了哪些输入值。
2. **Substitution（替换）**: 匹配替换是否改变指定端点；不能建立任务收益或一般音频使用。
3. **Benefit（收益）**: 匹配留出误差比较；不能说明机制。
4. **Endpoint validity（端点有效性）**: 控制能否排除指定捷径；不能保证检查端点之外的 validity。
在留出评分前固定划分、干预、分数、聚合单元和决策规则。门控按目标解释选择，通过一个门控不证明另一个。

## 实验与关键结果
### 1) 静态与时间人脸栅格检查
- **CREMA-D 静态栅格**: 73 演员开发、9 验证、9 密封确认；用 0.25s 身份栅格与 0.75–1.25s log-mel 预测 1.0s 的 64×64 栅格；评估 732 确认片段。对齐 MAE=0.02907。零音频 +0.131475 [0.127163, 0.135640]；演员音频替换 +0.000109 [0.000034, 0.000186]；身份栅格替换 +0.064860 [0.062795, 0.066897]。跨演员音频效应满足符号检测规则，但效应很小且未注册任务尺度阈值，实际意义未分类。
- **时间渲染器**: 5,038 开发、689 验证、708 密封序列；对齐 MAE=0.030449；音频平移使其升高 0.0000176；重复身份栅格使其降低 0.010592。没有区间或实际 margin，不能建立序列级音频收益。
- **RAVDESS 确认**: 240 对，2.0s 目标；对齐 MAE=0.08990；零音频 +0.20931 [0.20469,0.21358]；另一演员音频 -0.00045 [-0.00129,0.00039]，注册替换规则失败。常量音频拟合 0.08652 优于音频训练拟合 0.08990（四个匹配种子），表明时间端点上音频训练拟合反而更差。

### 2) 合成音频特征混合
205/24/27 源片段，零跨划分源片段、原始视频组、视频命名说话人、精确目标重叠。条件增强拟合在 1,000 步时 RMSE 高于仅音频拟合（0.1807 vs. 0.1707），但差距随训练缩小；显示活跃条件分支、策略依赖控制，以及在单独标量端点上的 condition-only 警告。

### 3) SpeakerVid 代理研究
源视频不相交的 SpeakerVid 代理，五臂五种子控制矩阵，四平台执行重复，事后检查四个留出源视频组。五特征置零拟合（五个低级音频摘要置零，保留 identity、dialogue、condition 输入）在四个留出条件和五个配对上，整帧灰度 RMSE 低于对齐音频；但对齐音频的 segment-drift 误差更低。说明输出激活、留出误差和端点控制在这些代理任务上支持不同解释。

## 贡献与局限
- 贡献：提出 CIViC 四问诊断框架；CREMA-D 演员不相交栅格检查；合成音频特征研究；SpeakerVid 源视频不相交代理研究。
- 局限：CIViC 不建立四个检查在测试设置外的必要或充分性；检测只排除命名的替代解释；实际使用需要任务尺度阈值或等价区域；重复种子/硬件不增加独立演员或源视频；CREMA-D 小效应未做实际分类；Study II 三种子结果只是固定运行方向，不做总体推断。

## 一句话评价
CIViC 是一个有价值且可证伪的音频条件视觉预测诊断协议，用四重证据门控揭示常见“移除/替换音频”实验的不足，并在多个代理任务上显示激活、留出收益与端点有效性可能彼此矛盾；但它边界明确、不提出新架构，实际阈值缺失使其更像评估纪律工具而非通用标准。

---

## 43. Explore This! Beat and Downbeat Tracking From a Learned Tatum Grid

**作者**: Robert Kihlborg, André Holzapfel, Jan Schlüter
**链接**: [2610.14817](https://arxiv.org/abs/2610.14817)
**分类**: Music Information Retrieval (Beat and Downbeat Tracking) | **关键词**: Beat Tracking, Downbeat Tracking, Tatum Grid, Transformer, Differentiable Music Theory, Dynamic Bayesian Network

# 论文总结：Explore This! Beat and Downbeat Tracking From a Learned Tatum Grid

## 核心痛点
- 当前 SOTA 节拍/重拍跟踪大多将 beat 和 downbeat 建模为独立事件，输出逐帧激活概率，再用 DBN 或局部极大值后处理。
- 独立逐帧概率无法表达不同节拍层级之间的依赖，也无法处理节拍歧义（metric ambiguity）：一个在 A/B 之间模糊的样本与一个在 C/D/E/F 之间模糊的样本会产生相同的局部概率（图1）。
- DBN 常假设恒定拍号；DBN-free 方法虽无此约束，但容易出现重复或缺失重拍。
- 常用评价指标 F-score 也把 beat/downbeat 当独立事件，且数据集严重偏向恒定拍号：97.7% 的训练曲目每分钟少于一次拍号变化，85% 为 4/4，9.6% 为 3/4。AMLt 也偏向二/四分组，对 12/8 等三分组不友好。
- 数学上理想的做法是建模整首乐曲所有可能标注的完整分布，但组合爆炸不可行；已有方法通过因子分解忽略依赖。

## 方法创新
- 提出介于逐帧独立概率和完整联合分布之间的分解方式：假设标注可分解为局部规则脉冲（tatum grid）和基于该脉冲表示的局部速度与拍号（subgrid，是 tatum 的子集而非细分）。
- 模型基于 Beat This! 的 Transformer 架构：前端 + 前 3 个 Transformer block 后接 Grid 模块预测 tatum grid，再经过 3 个 Transformer block 后接 Subgrid 模块预测 beats/downbeats，输出更接近 bar-pointer-like 的多选项节拍结构。
- Grid 模块将 tatum 表示为局部 tempo 和 phase，而非独立逐帧概率。输入按 1 秒窗口切分，每个窗口渲染局部 tempo/phase 的正弦波，并以 soft recall（在真实 beat 位置评估正弦波均值）为可微训练目标。为缓解 soft recall 非凹性，使用 mixture-of-experts：12 个候选波覆盖 12 个不重叠 tempo 区间（每区间 1/3 八度，总跨度 30–480 pulses/min），每个候选有 tempo 和 phase 参数，12 路 softmax 给出权重。
- 为保持节拍层级一致，加入相邻窗口不一致性损失：通过相位跳变和 tempo 差定义候选间不一致性，使用 soft clamping，并以 Sinkhorn 算法可微计算 12 个加权候选集合两两之间的 Earth Mover's Distance。
- 整体是深度学习与可微的、基于音乐理论模块的结合，输出比现有模型更具表达力，可支持多种拍号解释。

## 实验结果
- 与 Beat This! 直接比较：在 beat 上性能相当；在 downbeat 上，尤其对拍号变化的曲目，连续性指标（continuity metrics）显著更高。
- 相比现有 DBN-free 系统，连续性指标更好；比事实标准 DBN 更通用、更灵活，但平均而言仍落后于最佳 DBN-based 方法。
- 作者指出尚未触及 grid-subgrid 架构的性能上限：估计的 tatum grid 有时未能包含真实 beat；最终估计的节拍分布常随时间不一致，尤其在拍号变化时。解决任一问题应能提升整体性能。
- 代码已公开：https://github.com/CPJKU/explore_this

## 一句话评价
该论文探索了一种从可学习 tatum grid 出发、以可微模块联合建模局部 tempo/拍号并分组得到 beat/downbeat 的新范式，在重拍连续性和拍号变化场景上展现潜力，但受限于数据偏差和 grid/subgrid 估计误差，整体平均性能尚未超越最佳 DBN 方法，属于有前景但未完全兑现的探索性工作。

---

## 44. Two-Stage Multi-modal Learning for Dynamic Audio-Visual Navigation: From Physical Alignment to Scene Aggregation

**作者**: Jia Li, Yinfeng Yu
**链接**: [2610.14077](https://arxiv.org/abs/2610.14077)
**分类**: Audio-Visual Navigation | **关键词**: Dynamic Audio-Visual Navigation, Cross-Modal Fusion, Reinforcement Learning, Intensity-Calibrated Geometry Encoder, Cross-Modal Scene Aggregator

## 核心痛点

- **静态假设失效**：现有 Audio-Visual Navigation (AVN) 工作大多假设声源静止，而真实场景中目标往往持续移动（如行人、移动设备），由此引出更具挑战性的 **Dynamic Audio-Visual Navigation (D-AVN)** 任务，要求智能体在时变观测下推断声源运动并实时调整策略。
- **语义中心范式泛化差**：现有 D-AVN 方法高度依赖训练数据中学到的声音语义特征（如类别特定的频谱模式），对未见过的声音类别或分布外声音泛化能力弱，且忽略了与声传播物理规律一致、类别无关的线索——尤其是**声强与环境几何之间的关系**。
- **多模态融合过于粗糙**：主流方法采用简单的后期融合（特征拼接、对全局嵌入的粗粒度注意力），这类静态融合无法保留听觉与视觉之间的细粒度空间对应关系，限制了动态环境下的状态推理与鲁棒规划。

## 方法创新

论文提出 **Two-Stage Multi-modal Learning** 框架，将多模态推理分解为“物理对齐”和“场景聚合”两个阶段：

1. **Stage I：Physical Alignment（物理对齐）**
   - 提出 **Intensity-Calibrated Geometry Encoder (ICGE)**，对声强与深度几何进行像素级融合，学习**类别无关的 intensity–geometry 共现关系**，实现物理信息引导的对齐，从而捕捉与声传播物理规律一致的空间对应。

2. **Stage II：Scene Aggregation（场景聚合）**
   - 设计基于 Transformer 的 **Cross-Modal Scene Aggregator (CMSA)**，在保持空间结构的前提下，让多模态空间 token 进行动态、细粒度的跨模态交互，构建鲁棒的状态表示，克服静态后期融合的局限。

3. **Policy Learning**：将聚合后的状态映射为导航动作。

## 实验结果

- 在 **Replica** 与 **Matterport3D** 两个逼真 3D 环境（基于 Habitat + SoundSpaces 声学模拟器）上进行大量实验。
- 方法在 **成功率 (success rate)** 上达到 **SOTA**，并在复杂环境与**未听过声音类别 (unheard sound)** 场景下显著提升泛化能力与导航效率。
- 实验设置包含干扰声源、次级目标信号、时频掩码输入增强等复杂声学扰动，验证了框架的鲁棒性。

## 一句话评价

该工作通过“物理对齐 + 场景聚合”的两阶段多模态学习，将类别无关的声强–几何物理先验与 Transformer 细粒度跨模态融合相结合，为动态视听导航提供了一种兼顾泛化性与鲁棒性的新范式，在 D-AVN 任务上取得了 SOTA 表现。

---

## 45. Hearing's Blind Spots: Toward Perceptual Compute Allocation in Neural Text-to-Speech

**作者**: Aayush Gupta
**链接**: [2610.14056](https://arxiv.org/abs/2610.14056)
**分类**: Text-to-Speech | **关键词**: Perceptual Compute Allocation, Neural Text-to-Speech, Auditory Masking, Psychoacoustic Model, Waveform Decoder, Dynamic INT8 Quantization, PESQ

# Hearing's Blind Spots: Toward Perceptual Compute Allocation in Neural Text-to-Speech

## 核心痛点
- TTS 合成器会生成非常详细的波形，但听者并不需要感知所有细节。强声会掩蔽邻近弱声，形成上下文相关的“听觉盲区”。
- 传统神经声码器/波形解码器对输出位置采用固定网络结构，未根据感知重要性动态分配计算。
- 论文要研究的第一步不是在线省算，而是：在已完成合成的语音上，固定频谱退化预算的“放置位置”如何影响基于参考的质量分数。
- 原研究问题中，H1（感知冗余）仍未作为定量人类感知结论解决；H2（透明质量下降低端到端 CPU 时间）未被证明；H3（掩蔽引导分配优于能量/随机分配）在 oracle 比较中未获支持。
- 心理声学阈值是模型预测，负 headroom 不等于对特定听者、播放电平或同时删除集合不可闻；PESQ 也不能单独证明透明性或可懂度。

## 方法创新与贡献
- 提出 oracle 删除/噪声整形测试框架：在已合成语音的 STFT 时频 bin 上，按低能量优先、掩蔽 headroom 优先或随机排列进行删除；或在匹配 NSR 下按能量、掩蔽阈值、均匀方式分配噪声。
- 对比 Piper（VITS + HiFi-GAN，22.05 kHz）与 Kokoro v1.0（StyleTTS2 相关架构 + iSTFTNet，24 kHz），使用 ONNX Runtime CPU 推理。
- 语料包含 45 条文本：15 条对话代理提示（含数字和实体）、15 条叙事、15 条罗马化 Hindi-English（Hinglish）；两模型共 90 条波形。
- 使用 from-scratch Model-1 谱系心理声学实现与 spreading-matrix 实现；删除比较采用 leave-self-out 阈值以缓解自掩蔽，spreading-matrix 使用全局 -16 dB 阈值偏移。
- 质量评估：原始波形为参考，重采样到 16 kHz 后计算 wideband PESQ 和 STOI；分析使用 1024 点 Hann 窗、512 hop。
- 贡献包括：1）两个 TTS 模型家族中能量、掩蔽、随机删除策略的 oracle 对比；2）校准诊断与算子设计观察，说明为何模型声明的掩蔽比例不能自动视为可感知去除；3）CPU profiling 及 dynamic-INT8 Kokoro 解码器的负结果；4）开源脚本、结果文件、音频示例和听测工具。

## 实验结果
- 删除策略：在匹配目标 bin 比例下，能量排序删除在报告设置中平均 PESQ 最高，掩蔽准则次之，随机删除最差。
- 50% 删除的 spreading-matrix 对比：Piper 上能量/掩蔽/随机分别为 4.46、3.60、1.19；Kokoro 上分别为 3.42、2.10、1.22。
- 能量减掩蔽的 PESQ 差距从 Piper 10% 删除时约 0.009 到 Kokoro 50% 删除时约 1.316；配对 Wilcoxon 检验 p 值约 1.2e-7 到 5.7e-14，但属于探索性、未校正检验。
- 校准诊断显示阈值敏感；作者单人听测 pilot 未能建立透明的删除预算。
- CPU profiling：波形解码器是最大 kernel 时间组件。Piper HiFi-GAN 解码器占 69.5% Apple M5 Pro、63.3% Intel Xeon 8488C；Kokoro iSTFTNet 解码器占 95.6%、93.9%。RTF 摘要：Piper 0.018/0.023，Kokoro 0.156/0.194（Apple/Intel）。
- dynamic-INT8 Kokoro 解码器在两个 CPU 上均慢于 FP32，形成实现相关的负结果，并区分“输出冗余”与“实际节省计算”。
- 局限：决策使用已合成音频，因此不证明在线可跳过计算；质量指标在 16 kHz 评估，原生高于 8 kHz 的内容不在评分带宽内；删除预算是输出退化预算而非等计算预算；随机删除只是放置控制。

## 一句话评价
论文将“听觉盲区”用于 TTS 计算分配的设想推进到 oracle 输出退化研究：低能量优先删除是强基线，但掩蔽引导并未优于能量排序，且尚未证明任何真实计算节省或人类透明性。

---

