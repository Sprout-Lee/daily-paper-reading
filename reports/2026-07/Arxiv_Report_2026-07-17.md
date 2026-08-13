# Arxiv Daily Deep Report - 2026-07-17

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 5
---

## 1. What does the model actually see? Evaluation protocols and input availability in data-driven prediction of room acoustic parameters

**作者**: Akın Oktav
**链接**: [2607.15243](https://arxiv.org/abs/2607.15243)
**分类**: Room Acoustics / Machine Learning Evaluation | **关键词**: ISO 3382-1, machine learning, evaluation protocols, cross-validation, data leakage

## 核心痛点
论文指出，基于机器学习的房间声学参数预测模型常报告高决定系数（R²>0.85），但这些高精度往往源于评估协议中的两种数据泄露：1）**验证分割方式**：行级随机分割使同一接收位置的不同测量出现在训练和测试集，导致条件插值而非空间预测；2）**输入特征可用性**：包含目标位置自身的脉冲响应等测量值，相当于提供了位置指纹，泄露了目标信息。

## 方法创新
- **因子化协议消融**：系统比较了两种分割方式（行级随机 vs. 按接收位置分组）和两类输入（完整特征 vs. 仅几何+环境）的组合，量化协议对性能的影响。
- **混合CNN模型**：融合几何分支和梅尔频谱分支，并分析其利用目标脉冲响应作为位置指纹的行为。
- **提出评估清单**：基于实验结果，建议在数据驱动房间声学研究中明确报告分割方式和输入可用性。

## 实验结果
- 在264座会议厅数据集上，行级分割+完整输入得到核心参数平均R²=0.81；分组分割+仅几何环境输入使R²降至0.09-0.57，参数难度排序改变。
- 混合CNN在目标脉冲响应作为输入时，行级分割下表现良好，但分组分割下性能下降，说明其利用了位置指纹而非可迁移声学信息。
- 在诚实协议下（分组分割+仅几何环境输入），随机森林、混合CNN和逆距离加权模型的性能差异比同一模型在不同协议下的差异小一个数量级；学习模型在声强和混响时间上仍有优势。

## 一句话评价
本文通过严谨的协议消融实验，揭示了房间声学参数预测中数据泄露的普遍性及影响，为可靠评估提供了方法论指导。

---

## 2. SLT 2026 REAL-TSE Challenge: Real-world Target Speaker Extraction from Conversational Recordings

**作者**: Shuai Wang, Zihan Qian, Ke Zhang, Jiangyu Han, Zikai Liu, Xiaoyang Yu, Haoyu Li, Marc Delcroix, Kai Yu, Lei Xie, Ming Li, Haizhou Li
**链接**: [2607.15198](https://arxiv.org/abs/2607.15198)
**分类**: Target Speaker Extraction | **关键词**: Target Speaker Extraction, Real-world, Conversational Recordings, Online vs Offline, Multi-metric Evaluation, REAL-TSE Challenge, BSRNN

## 核心痛点
当前的TSE评估主要依赖模拟混合数据（如LibriMix、WSJ0-2Mix），无法真实反映实际对话中的自然重叠、混响、噪声、通道失配和对话动态等问题。

## 方法创新
- **双轨设置**：在线流式（延迟≤100ms）与离线全上下文处理。
- **多维评估指标**：Token Error Rate (TER)、Speaker Similarity (SpkSim)、DNSMOS (P808)、目标说话人活动F1。
- **真实数据**：使用REAL-T等真实对话录音，包含中英文，并分开发集、EVAL-1（同域）和EVAL-2（新域，含多种通道匹配）。
- **开放训练策略**：无官方训练集，允许使用开源数据和预训练模型。

## 实验结果
- 共收集24个系统（18个团队），在线/离线各12个有效提交。
- 顶级系统大幅超越基线（BSRNN系列），但在不同指标上表现互补，无单一系统全面领先。
- 指标间存在权衡，如TER与F1、SpkSim与DNSMOS。

## 一句话评价
该挑战赛通过真实对话数据和多维度评估，为实际场景下的目标说话人提取提供了更全面的基准。

---

## 3. WanSong v1.0 Technical Report

**作者**: Binghui Chen, Pandeng Li, Yu Liu, Jingren Zhou
**链接**: [2607.14749](https://arxiv.org/abs/2607.14749)
**分类**: Music Generation | **关键词**: WanSong, 扩散模型, 双音轨, MMDit, 强化学习, 文本到音乐

## 核心痛点
现有音乐生成模型大多基于自回归（AR）建模或级联多阶段流水线（如AR+扩散），导致生成效率低、长音频质量不一致，且难以在可控性、高保真度与长时长之间取得平衡。

## 方法创新
1. **纯扩散框架**：将音频视为连续token，采用端到端单阶段扩散模型，摒弃传统AR范式。
2. **双音轨建模**：独立建模人声（vocal）和背景音乐（BGM）token，消除二者间干扰，并直接输出分离音轨，便于后期编辑。
3. **混合MMDit架构**：结合Transformer与MMDit，采用全共享AdaLN减少参数，通过打包策略提高token吞吐量。
4. **强化学习对齐**：使用DPO和ReFL两阶段训练，针对音乐性、歌词准确性和提示对齐三个维度优化模型。
5. **多阶段训练**：预训练包含90秒、300秒和SFT阶段，逐步学习长时长歌曲细节。

## 实验结果
- VAE在压缩率1024下，音乐基准STFT距离1.029、SI-SDR 7.246dB，优于Stable Audio 2。
- 完整模型支持5分钟多语言歌曲生成，双音轨输出。

## 一句话评价
WanSong v1.0通过纯扩散框架和双音轨建模，实现了高效、高保真、可控的长时长歌曲生成，是音乐生成领域的重要突破。

---

## 4. Dialogs: a studio-quality expressive conversational Russian speech corpus for dialog assistants

**作者**: Ilya Shigabeev, Ilya Latyshev
**链接**: [2607.14310](https://arxiv.org/abs/2607.14310)
**分类**: Text-to-Speech | **关键词**: conversational speech corpus, expressive TTS, Russian, dialog assistants, VITS2, crowd MOS, audio quality, emotion labels

# Dialogs：用于对话助手的录音室质量、富有表现力的俄语会话语音语料库

## 核心痛点
- 俄语缺乏高质量的会话语音语料库：现有俄语资源要么是单说话人朗读语音（如Ruslan、Natasha），缺乏情感变化；要么是网络采集数据（如Golos），录音条件不受控，转录质量受ASR限制。对于训练富有表现力、对话风格的TTS系统，现有数据无法满足需求。

## 方法创新
- 构建了Dialogs语料库：20.6小时，三说话人（1男2女），专业录音室立体声录制（44.1kHz），包含11,796个话语。
- 录制方式：演员面对面进行脚本对话，允许即兴发挥，产生自然的轮流节奏和富有表现力的韵律。
- 标注：通过众包平台对每个话语标注12种风格/情感类别（中性、高兴、惊讶、悲伤、厌恶、生气、绕口令、诗歌、耳语、傲慢、大笑、恐惧），采用多数投票和稀有类别优先处理平局。
- 质量验证：通过众包MOS测试，Dialogs在音频质量和可懂度上与Ruslan、Natasha相当，但在表现力和对话自然度上显著更高（+0.23-0.30分）。
- 作为概念验证，在Dialogs上训练VITS2模型，证明其可用于训练富有表现力的对话TTS。

## 实验结果
- 语料库MOS：总体4.15，音频质量4.19，韵律4.05，可懂度4.14，表现力4.11，对话自然度4.08。
- VITS2合成语音MOS：总体2.83，音频质量2.97，韵律2.55，可懂度2.28，表现力2.56，对话自然度2.59。UTMOS 3.36。
- 合成语音展现了对话风格，但评分较低，原因是每个说话人数据量有限（4.4-9.9小时）。

## 一句话评价
Dialogs是俄语首个结合录音室质量、对话风格和情感标注的开源语料库，为对话TTS提供了重要资源，但说话人数据不均限制了单独使用效果。

---

## 5. MIDI-RAE-JEPA: Hierarchical Representation Learning and Generation for Symbolic Music

**作者**: Scott H. Hawley
**链接**: [2607.14537](https://arxiv.org/abs/2607.14537)
**分类**: Symbolic Music Representation Learning and Generation | **关键词**: symbolic music, self-supervised learning, equivariance, hierarchical representation, representation autoencoder

## 核心痛点
当前符号音乐表示学习缺乏层次化自监督方法，现有模型难以捕捉音乐的多尺度层次结构（如音符、乐句、乐段），且基于自然图像的SSL方法（如DINOv2）不适用于钢琴卷帘图（piano roll），因为其尺度变换会破坏音乐结构。

## 方法创新
提出**MIDI-RAE-JEPA**，结合等变性目标（pitch和time shift）、LeJEPA框架和Swin Transformer V2编码器，学习符号音乐的层次化表示。主要贡献包括：
- **等变性损失**：使用delta-scaled目标距离，使嵌入距离与位移幅度成正比，防止坍缩。
- **软分解损失**：在潜在空间中强制pitch和time方向几何正交。
- **分块SIGReg**：减少显存占用并提高吞吐量。
- **EMA教师+掩码嵌入预测器**：提供稳定目标并促进上下文预测。
- **完整RAE流水线**：编码器+冻结编码器解码器+条件流匹配生成模型，实现重建和生成。

## 实验结果
- 重建F1分数达0.995。
- 条件生成能匹配条件片段的音高注册和节奏密度。
- 在下游情感分类任务中，表示优于Haar散射变换基线。
- 嵌入距离随pitch和time位移单调增加，验证了等变性。
- 所有实验在消费级GPU（RTX 4090等）上运行。

## 一句话评价
MIDI-RAE-JEPA首次将层次化JEPA方法应用于符号音乐，通过等变性自监督学习获得语义丰富且可用于生成的表征。

---

