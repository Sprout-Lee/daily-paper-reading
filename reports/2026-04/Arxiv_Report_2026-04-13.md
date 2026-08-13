# Arxiv Daily Deep Report - 2026-04-13

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 8
---

## 1. Data Selection Effects on Self-Supervised Learning of Audio Representations for French Audiovisual Broadcasts

**作者**: Valentin Pelloin, Lina Bekkali, Reda Dehak, David Doukhan
**链接**: [2604.09472](https://arxiv.org/abs/2604.09472)
**分类**: Audio Representation Learning | **关键词**: self-supervised learning, pretraining dataset, audio encoders, speech, music

# 论文总结：Data Selection Effects on Self-Supervised Learning of Audio Representations for French Audiovisual Broadcasts

## 核心痛点
- 当前自我监督学习（SSL）音频模型通常在干净、分割的语音数据（如LibriSpeech）上训练，忽视了多样音频内容（如音乐、噪音）。
- 存在性别偏见问题，模型性能可能因训练数据不平衡而受影响。
- 数据重复问题可能导致模型记忆敏感信息，影响泛化能力和隐私安全。

## 方法创新
- 构建了一个大型、多样化的法国视听广播音频语料库：从法国国家视听研究所（INA）获取473k小时数据，经去重和预处理后，形成100,000小时的预训练语料库。
- 使用自动工具（如Whisper进行转录和语言识别，InaSpeechSegmenter进行语音活动和性别分割，以及基于music2vec的音乐检测模型）描述音频内容。
- 创建了六个1,000小时的子集（如base、no_music、only_speech、only_fr、gender、duplicates），以评估数据选择对SSL模型性能的影响。
- 进行了预训练和下游任务评估，包括自动语音识别、语音活动检测、音乐检测、说话人识别，以及成员推理攻击来评估数据记忆风险。

## 实验结果
- 预训练在多样音频内容上的SSL模型在多种下游任务中表现出潜力，无需限制为纯语音数据。
- 数据去重被证明能有效减少模型记忆训练数据，提升隐私安全性。
- 具体性能数字未在片段中提供，但摘要指出该方法有望桥接语音和音乐机器学习社区。

## 一句话评价
这项研究通过利用法国视听广播的多样音频内容，推动了统一音频表示学习的发展，并为数据选择和去重在SSL中的重要性提供了实证见解。

---

## 2. Discrete Token Modeling for Multi-Stem Music Source Separation with Language Models

**作者**: Pengbo Lyu, Xiangyu Zhao, Chengwei Liu, Haoyin Yan, Xiaotao Liang, Hongyu Wang, Shaofei Xue
**链接**: [2604.09371](https://arxiv.org/abs/2604.09371)
**分类**: Music Source Separation | **关键词**: Discrete Token Modeling, Music Source Separation, Language Models, Generative Framework, HCodec, Conformer, Autoregressive Generation

# 详细总结

## 核心痛点
- 音乐源分离（MSS）任务复杂，音频信号高维且变化多样，现有方法多为判别性，直接估计连续频谱或波形，受限于回归式建模的局限性。
- 现有离散令牌方法（如TokenSplit、TSELM、UniSep）主要针对单一目标源提取，而非多轨同时分离，难以处理多轨依赖关系。

## 方法创新
- 提出生成性框架，将MSS重新定义为条件离散令牌生成任务，避免了直接回归连续信号的挑战。
- 结合Conformer-based条件编码器提取混合音频特征，HCodec（双路径神经音频编码器）将连续音频编码为声学和语义离散令牌序列。
- 使用仅解码器语言模型（基于LLaMA架构）自回归生成四轨令牌（人声、鼓、贝斯、其他），顺序生成以建模跨轨道依赖。
- 训练时采用教师强制和加权损失，推理时自回归生成令牌并通过HCodec解码回波形。

## 实验结果
- 在MUSDB18-HQ基准上评估，使用感知指标如ViSQOL、DNSMOS和NISQA，避免了对齐样本的局限性。
- 生成性方法在ViSQOL分数上接近最先进的判别方法（如HTDemucs、BS-RoFormer、SCNet），表明离散令牌建模的有效性。
- 人声轨道获得最高NISQA分数（2.50），突显了在感知质量上的优势。
- 消融研究验证了可学习Conformer编码器和顺序跨轨道生成的重要性，确认了方法的贡献。

## 一句话评价
该方法创新地利用离散令牌和语言模型，实现了高质量的多轨音乐源分离，为生成性音频处理开辟了新途径。

---

## 3. Phonemes vs. Projectors: An Investigation of Speech-Language Interfaces for LLM-based ASR

**作者**: Ziwei Li, Lukuang Dong, Saierdaer Yusuyin, Xianyu Zhao, Zhijian Ou
**链接**: [2604.09332](https://arxiv.org/abs/2604.09332)
**分类**: Speech Recognition | **关键词**: large language models, LLM-ASR, speech-language interface, phoneme, projector, BPE-phoneme

## 核心痛点
LLM-based ASR（基于大语言模型的自动语音识别）的性能和数据效率高度依赖于 speech-language 接口设计。常见方法是使用学习型投影器将语音特征映射到 LLM 嵌入空间，但缺乏对连续（投影器）和离散（音素）接口的系统比较，特别是在高低资源设置下的差异。

## 方法创新
1. **系统比较两种接口**：使用相同的语音编码器和 LLM 骨干，对比 projector-based（连续）和 phoneme-based（离散）接口。
2. **提出 BPE-phoneme 接口**：合并高频局部音素模式，同时保留显式词边界线索，以改进音素到字形的生成。
3. **引入 phoneme-informed hybrid 接口**：通过音素监督初始化编码器，再用于投影器路径，结合两种方法的优势。

## 实验结果
- **高资源英语（LibriSpeech）**：Phoneme-based 接口与 vanilla projector 竞争；BPE-phoneme 接口带来进一步增益。
- **低资源 Tatar（20小时）**：Phoneme-based 接口显著优于 vanilla projector。
- **混合接口**：Phoneme-informed hybrid 接口比 vanilla projector 更强。

## 一句话评价
这项研究系统性地评估了 LLM-based ASR 中的 speech-language 接口，展示了音素基方法在低资源设置下的优越性，为接口设计提供了新见解。

---

## 4. PS-TTS: Phonetic Synchronization in Text-to-Speech for Achieving Natural Automated Dubbing

**作者**: Changi Hong, Yoonah Song, Hwayoung Park, Chaewoon Bang, Dayeon Gu, Do Hyun Lee, Hong Kook Kim
**链接**: [2604.09111](https://arxiv.org/abs/2604.09111)
**分类**: Automated Dubbing and Speech Synchronization in Text-to-Speech | **关键词**: Automated Dubbing, Lip-Synchronization, Phonetic Synchronization, Text Paraphrasing, Cross-lingual Text-to-Speech

# 论文总结

## 核心痛点
自然自动配音（Automated Dubbing, AD）面临同步挑战，特别是持续时间同步（isochrony）和嘴唇同步（lip-sync），这对保持观看体验至关重要。现有方法在语言结构不同时难以实现准确的嘴唇同步，且可能影响语义保留。

## 方法创新
本文提出 PS-TTS 方法，包括两个主要步骤：
1. **Isochrony (ISO)**：通过神经机器翻译（NMT）对源文本进行翻译，并使用 TTS 持续时间预测器选择与源语音持续时间最匹配的候选文本，实现时间对齐。
2. **Phonetic Synchronization (PS)**：使用动态时间规整（DTW）基于元音距离评估语音相似性，选择发音相似的目标文本。进一步提出 **PS-Comet**，结合 COMET 语义相似性度量，在保持嘴唇同步的同时更好地保留意义。

## 实验结果
在韩语和英语唇读数据集、配音演员数据集上评估。PS-TTS 和 PS-Comet TTS 在客观指标（如嘴唇同步错误置信度 LSE-C、距离 LSE-D 和 UTMOS）上优于没有 PS 的基线 TTS 系统，并在韩英和英韩配音中超过专业配音演员。实验扩展到法语，测试所有语言对，PS-Comet 在所有情况下表现最佳，平衡了嘴唇同步准确性和语义保持。

## 一句话评价
PS-Comet 通过整合语音和语义相似性，实现了更准确、自然的自动配音，适用于跨语言应用。

---

## 5. Enhancing Conversational TTS with Cascaded Prompting and ICL-Based Online Reinforcement Learning

**作者**: Zhicheng Ouyang, Seong-Gyun Leem, Bach Viet Do, Haibin Wu, Ariya Rastrow, Yuzong Liu, Florian Metze
**链接**: [2604.08709](https://arxiv.org/abs/2604.08709)
**分类**: Text-to-Speech | **关键词**: Conversational AI, in-context learning, expressive synthesis, controllable TTS, online reinforcement learning

## 核心痛点
对话AI中，生成表达性和可控的文本到语音（TTS）仍然具有挑战性。主要问题在于细粒度语音风格和情感的控制，传统上需要大量标注的训练数据，导致数据瓶颈和扩展困难。

## 方法创新
论文提出一个可扩展且数据高效的级联框架，结合文本风格令牌和高质量音频提示。音频提示作为上下文学习（ICL），在推理时引导模型的韵律和音色，无需权重更新。此外，引入基于ICL的在线强化学习（RL）策略，使用主观美学奖励（AES-CE）优化自回归韵律模型，同时通过CTC对齐防止幻觉，确保可理解性。

## 实验结果
通过全面的人类感知评估，论文展示了显著改进。在自然性方面，ICL模型相比零基线有+7.5%的净胜率（CMOS）；在表达性（CV AD维度）方面，相比零基线有+79.6%的改进，相比GPT-4o有+5.6%的改进。这些结果证实了方法的有效性。

## 一句话评价
该研究通过级联提示和基于ICL的在线RL，为对话TTS提供了高效且可控的解决方案，在自然性和表达性方面均有显著提升。

---

## 6. DialogueSidon: Recovering Full-Duplex Dialogue Tracks from In-the-Wild Dialogue Audio

**作者**: Wataru Nakata, Yuki Saito, Kazuki Yamauchi, Emiru Tsunoo, Hiroshi Saruwatari
**链接**: [2604.09344](https://arxiv.org/abs/2604.09344)
**分类**: Audio Enhancement | **关键词**: full-duplex dialogue, speech restoration, joint separation and restoration

## 详细总结

### 核心痛点
全双工对话音频（每个说话者单独轨道）对口语对话研究至关重要，但难以大规模收集，因为大多数野外双人对话音频是退化的单声道混合，包含背景噪声、混响和压缩伪影。现有语音分离方法通常基于单声道清洁语音，不适用于自发对话音频中的重叠模式、韵律和互动时机差异。

### 方法创新
论文提出DialogueSidon模型，用于从退化的单声道双人对话音频中联合恢复和分离出清洁的全双工轨道。方法结合两个核心组件：
- **SSL-VAE**：基于自监督学习（SSL）模型特征（如w2v-BERT 2.0）的变分自编码器，将高维SSL特征压缩成紧凑潜在空间，适用于扩散建模。
- **扩散基潜在预测器**：估计说话者特定的潜在表示从退化混合中，然后通过SSL-VAE解码器重构波形。
模型分两阶段训练：第一阶段训练SSL-VAE构建潜在空间；第二阶段训练潜在预测器，使用低秩适应（LoRA）等技术优化。

### 实验结果
在英语、多语言和野外对话数据集上的实验显示，DialogueSidon在可懂度和分离质量上显著优于基线方法（如统一恢复和分离基线），同时实现更快的推理速度。结果强调了模型在内容保存和分离效果方面的改进。

### 一句话评价
DialogueSidon是一个创新的模型，有效解决了从野外对话音频中恢复高质量全双工轨道的挑战，通过结合SSL-VAE和扩散模型，推动了对话语音研究的数据可用性和系统性能。

---

## 7. Script Collapse in Multilingual ASR: Defining and Measuring Script Fidelity Rate

**作者**: Hanif Rahman
**链接**: [2604.08786](https://arxiv.org/abs/2604.08786)
**分类**: Speech Recognition | **关键词**: Script Fidelity Rate, Script Collapse, Multilingual ASR, Evaluation Metrics, Non-Latin Scripts

### 核心痛点
Word Error Rate (WER) 作为自动语音识别（ASR）的主流评估指标，无法检测脚本崩溃（script collapse）现象，即模型在错误书写系统中产生流畅输出，而 WER 仍可能显示有限错误率，导致评估误导和实际部署中输出不可读。

### 方法创新
提出脚本保真率（Script Fidelity Rate, SFR），定义为假设字符串中目标脚本字符的比例，基于 Unicode 块成员资格计算，无需参考转录（reference-free）。SFR 补充了 WER，能直接量化脚本保真度，并满足有界性、单调性和可组合性等度量属性。

### 实验结果
在 FLEURS 测试集上评估六种语言（Pashto、Urdu、Hindi、Bengali、Malayalam、Somali）跨越四种书写系统，覆盖九个 ASR 模型（包括 Whisper 系列、MMS-1B、SeamlessM4T-v2）。在 53 个模型-语言对中，18 个（34%；95% Wilson CI: 23–47%）表现出脚本崩溃（SFR < 10%），主要涉及 Whisper 模型；MMS-1B 和 SeamlessM4T-v2 在所有评估语言上 SFR 高于 99%。识别出三种脚本崩溃模式：拉丁语音替代（较小 Whisper 模型在 Indic 语言）、阿拉伯语替代（用于 Somali 的拉丁书写）、以及德瓦纳加里替代（较大 Whisper 模型将所有 Indic 音频视为 Hindi）。

### 一句话评价
该研究为多语言 ASR 提供了一个有效的补充评估指标 SFR，系统揭示了脚本崩溃问题，有助于改进模型评估和部署中的脚本保真度。

---

## 8. Neural networks for Text-to-Speech evaluation

**作者**: Ilya Trofimenko, David Kocharyan, Aleksandr Zaitsev, Pavel Repnikov, Mark Levin, Nikita Shevtsov
**链接**: [2604.08562](https://arxiv.org/abs/2604.08562)
**分类**: Speech Quality Assessment | **关键词**: Text-to-Speech, Speech Quality Assessment, MOS, SBS, Self-Supervised Learning, Multimodal Learning, Ensemble Methods

# 核心痛点
人类主观评估 Text-to-Speech (TTS) 系统质量（如 Mean Opinion Score (MOS) 和 Side-by-Side (SBS) 比较）虽然被视为金标准，但成本高、速度慢、易受评估者偏差影响，制约了 TTS 系统的快速迭代和大规模应用。自动化评估的需求迫切，以填补传统客观指标与人类感知之间的鸿沟。

# 方法创新
本研究提出了一系列神经模型，旨在自动化 TTS 质量评估：
- **相对评估 (SBS)**: 引入 NeuralSBS，基于 HuBERT 编码器，通过反对称双线性层学习音频对之间的偏好概率，确保逻辑一致性（如 P(A > B) = 1 - P(B > A)）。同时探索了多模态变体 NeuralSBSBert，通过跨注意力融合 BERT 文本特征。
- **绝对评估 (MOS)**: 增强 MOSNet，采用序列长度批处理、掩码填充和序列级损失优化；引入 WhisperBert，一种多模态堆叠集成方法，结合 Whisper 音频特征和 BERT 文本嵌入，通过弱学习器和元学习器预测 MOS 分数。此外，尝试了基于 SpeechLM 的架构，但发现性能不佳。
- **数据预处理**: 使用数据标准化（Std SOMOS）减少评估者偏差，并应用信号和语音级数据增强。

# 实验结果
- **相对评估**: NeuralSBS 在 SOMOS 数据集上达到 73.7% 准确率和 0.816 AUC-ROC。多模态变体 NeuralSBSBert 表现略差，表明朴素跨注意力融合可能干扰音频特征；标准化数据集上性能下降，因分数方差压缩导致区分难度增加。
- **绝对评估**: WhisperBert 等 MOS 模型实现 RMSE ∼0.40，显著优于人类评估者间 RMSE 基线 0.62。实验显示，直接融合文本通过跨注意力可能降低性能，强调集成方法（如堆叠）的有效性。尝试的 SpeechLM 架构和零-shot LLM（如 Qwen2-Audio）性能不理想。

# 一句话评价
该研究通过创新神经模型为 TTS 自动化评估提供了高效、与人类判断高度对齐的解决方案，显著降低了评估成本并加速了 TTS 系统开发。

---

