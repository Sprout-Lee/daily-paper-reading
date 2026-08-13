# Arxiv Daily Deep Report - 2026-05-20

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 4
---

## 1. Cross-Talk Speech Reduction, by Separation, for Separation

**作者**: Zhong-Qiu Wang, Samuele Cornell
**链接**: [2605.19695](https://arxiv.org/abs/2605.19695)
**分类**: Speech Separation | **关键词**: cross-talk reduction, speech separation, pseudo-label, far-field, close-talk, CHiME-6

## 核心痛点
在对话语音分离中，远场麦克风捕获的混合信号与近场（close-talk）麦克风捕获的信号之间存在严重的域不匹配问题。近场信号虽然能量高，但包含大量来自其他说话人的串扰（cross-talk）和背景噪声，无法直接用作训练远场分离模型的伪标签。

## 方法创新
提出**跨说话人语音减少（Cross-Talk Reduction, CTR）**任务，旨在从每个近场混合中分离出佩戴者本身的语音。设计**CTRnet**，利用近场和远场混合信号对进行训练，包括无监督、弱监督和半监督变体。进一步提出**PuLSS（Pseudo-Label based far-field Speech Separation）**，将CTRnet估计的干净近场语音作为伪标签，用于训练远场语音分离模型。整个框架可直接在真实目标域数据上训练，避免了合成数据训练的泛化问题。

## 实验结果
在**CHiME-6**数据集上，PuLSS在Oracle和估计说话人日志条件下均取得了最先进的ASR性能，超越所有CHiME-7/8挑战提交结果。据作者所知，这是首个在真实“野”对话数据上显著优于引导源分离（GSS）的神经语音分离方法。

## 一句话评价
提出了一种利用近场麦克风信号作为弱监督信号进行远场语音分离的新框架，有效缓解了域不匹配问题，并在真实场景中取得突破性能。

---

## 2. Fast Multichannel NMF with Block-Diagonal Spatial Covariance Matrices for Efficient Blind Source Separation Using Distributed Microphone Arrays

**作者**: Hirotaka Nishikori, Nobutaka Ito, Kouei Yamaoka, Norihiro Takamune, Hiroshi Saruwatari
**链接**: [2605.19388](https://arxiv.org/abs/2605.19388)
**分类**: Blind Source Separation | **关键词**: Distributed Microphone Arrays, Blind Source Separation, Fast Multichannel Nonnegative Matrix Factorization, Block-Diagonal Spatial Covariance Matrix

## 核心痛点
分布式麦克风阵列的盲源分离（BSS）中，直接对全阵列应用FastMNMF计算成本随麦克风数量快速增长（O(IM⁴)），而只使用单个子阵列则无法利用其他子阵列的信息，分离性能受限。

## 方法创新
提出**Distributed FastMNMF**，在源空间协方差矩阵（SCM）上施加**块对角结构**，每个块对应一个子阵列，使得矩阵求逆和联合对角化仅在子阵列内进行。同时，NMF源谱图模型在所有子阵列间共享，从而聚合源活动信息而舍弃子阵列间协方差。

## 实验结果
在同步、无噪声的固定房间和阵列/源几何仿真中：
- 计算时间低于全阵列FastMNMF；
- 平均源失真比（SDR）高于单子阵列FastMNMF；
- 可应用于五源条件（每个子阵列4个麦克风，局部欠定）。

## 一句话评价
提出了一种计算高效且性能适中的分布式BSS方法，在计算复杂度和分离性能之间取得平衡。

---

## 3. Mega-ASR: Towards In-the-wild^2 Speech Recognition via Scaling up Real-world Acoustic Simulation

**作者**: Zhifei Xie, Kaiyu Pang, Haobin Zhang, Deheng Ye, Xiaobin Hu, Shuicheng Yan, Chunyan Miao
**链接**: [2605.19833](https://arxiv.org/abs/2605.19833)
**分类**: Error | **关键词**: 

总结生成失败: 'utf-8' codec can't encode character '\ud83d' in position 14452: surrogates not allowed

---

## 4. CounterFlow: A Two-Phase Inference-Time Sampling for Counterfactual Video Foley Generation

**作者**: Gyubin Lee, Junwon Lee, Juhan Nam
**链接**: [2605.18916](https://arxiv.org/abs/2605.18916)
**分类**: Video-to-Audio Generation / Counterfactual Foley | **关键词**: Counterfactual Video Foley Generation, Inference-Time Sampling, Flow Matching, Decomposed Guidance, Negative Prompting

## 核心痛点
现有视频文字到音频（VT2A）模型在处理矛盾视频和文本条件时，视觉线索主导采样轨迹，导致生成音频难以替换为反事实目标声音。

## 方法创新
提出 **CounterFlow**，一种无需重新训练的推理时两阶段采样方案：
- **Phase 1**：保留视频条件，使用分解引导（decomposed guidance）构建视频对齐的时间结构，同时通过源文本负提示抑制视觉隐含声源。
- **Phase 2**：移除视频条件，仅用文本条件和负提示精炼目标音色。
该方法基于预训练流匹配VT2A骨架（如MMAudio），通过阶段切换实现结构-身份分离。

## 实验结果
在VGGSound-Sparse Clean数据集上，CounterFlow在反事实替换质量（∆FLAM 0.2641，正比率92.0%）和整体质量（FAD 23.55，IS 7.915）上显著优于CAFA、ReWaS等基线，同时保持竞争性的时序对齐（DeSync 0.6695）。消融实验验证了分解引导和Phase 2负提示的必要性。

## 一句话评价
CounterFlow通过两阶段推理采样解耦了视觉时间结构与声音身份注入，实现了高质量的反事实视频拟音生成。

---

