# Amazon Braket Algorithm Library
[![Build](https://github.com/amazon-braket/amazon-braket-algorithm-library/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/amazon-braket/amazon-braket-algorithm-library/actions/workflows/python-package.yml)

> [!IMPORTANT]
> このリポジトリは[Amazon Braket Algorithm Library](https://github.com/amazon-braket/amazon-braket-algorithm-library)をNCDC環境用にforkしたものです。オリジナルのリポジトリから以下の改変を行っています：
> - uvを使用したパッケージ管理への移行
> - READMEの日本語化
> - その他NCDC環境に合わせたカスタマイズ

Amazon Braket Algorithm Libraryは、代表的な量子アルゴリズムと実験的なワークロードの実装をすぐに実行できるサンプルノートブックとして提供するライブラリです。

---
## 対応環境

現在、Braketアルゴリズムは以下のOS上でテストされています：
- Linux
- Windows
- macOS

ノートブックをローカルで実行する場合は、[notebooks/textbook/requirements.txt](https://github.com/amazon-braket/amazon-braket-algorithm-library/blob/main/notebooks/textbook/requirements.txt)にある追加の依存関係が必要です。詳細はnotebooks/textbook/README.mdを参照してください。

---
## 実装されているアルゴリズム

### 教科書的アルゴリズム

| アルゴリズム | ノートブック | 参考文献 |
| ----- | ----- | ----- |
| ベルの不等式 | [Bells_Inequality.ipynb](notebooks/textbook/Bells_Inequality.ipynb) | [Bell1964](https://journals.aps.org/ppf/abstract/10.1103/PhysicsPhysiqueFizika.1.195), [Greenberger1990](https://doi.org/10.1119/1.16243) |
| Bernstein-Vazirani | [Bernstein_Vazirani_Algorithm.ipynb](notebooks/textbook/Bernstein_Vazirani_Algorithm.ipynb) | [Bernstein1997](https://epubs.siam.org/doi/10.1137/S0097539796300921) |
| CHSH不等式 | [CHSH_Inequality.ipynb](notebooks/textbook/CHSH_Inequality.ipynb) | [Clauser1970](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.23.880) |
| Deutsch-Jozsa | [Deutsch_Jozsa_Algorithm.ipynb](notebooks/textbook/Deutsch_Jozsa_Algorithm.ipynb) | [Deutsch1992](https://royalsocietypublishing.org/doi/10.1098/rspa.1992.0167) |
| Groverの探索アルゴリズム | [Grovers_Search.ipynb](notebooks/textbook/Grovers_Search.ipynb) | [Figgatt2017](https://www.nature.com/articles/s41467-017-01904-7), [Baker2019](https://arxiv.org/abs/1904.01671) |
| QAOA（量子近似最適化アルゴリズム） | [Quantum_Approximate_Optimization_Algorithm.ipynb](notebooks/textbook/Quantum_Approximate_Optimization_Algorithm.ipynb) | [Farhi2014](https://arxiv.org/abs/1411.4028) |
| 量子回路ボルンマシン | [Quantum_Circuit_Born_Machine.ipynb](notebooks/textbook/Quantum_Circuit_Born_Machine.ipynb) | [Benedetti2019](https://www.nature.com/articles/s41534-019-0157-8), [Liu2018](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.98.062324) |
| QFT（量子フーリエ変換） | [Quantum_Fourier_Transform.ipynb](notebooks/textbook/Quantum_Fourier_Transform.ipynb) | [Coppersmith2002](https://arxiv.org/abs/quant-ph/0201067) |
| QPE（量子位相推定） | [Quantum_Phase_Estimation_Algorithm.ipynb](notebooks/textbook/Quantum_Phase_Estimation_Algorithm.ipynb) | [Kitaev1995](https://arxiv.org/abs/quant-ph/9511026) |
| 量子ウォーク | [Quantum_Walk.ipynb](notebooks/textbook/Quantum_Walk.ipynb) | [Childs2002](https://arxiv.org/abs/quant-ph/0209131) |
| Shorの素因数分解アルゴリズム | [Shors_Algorithm.ipynb](notebooks/textbook/Shors_Algorithm.ipynb) | [Shor1998](https://arxiv.org/abs/quant-ph/9508027) |
| Simonのアルゴリズム | [Simons_Algorithm.ipynb](notebooks/textbook/Simons_Algorithm.ipynb) | [Simon1997](https://epubs.siam.org/doi/10.1137/S0097539796298637) |

### 高度なアルゴリズム

| アルゴリズム | ノートブック | 参考文献 |
| ----- | ----- | ----- |
| 量子PCA（主成分分析） | [Quantum_Principal_Component_Analysis.ipynb](notebooks/advanced_algorithms/Quantum_Principal_Component_Analysis.ipynb) | [He2022](https://ieeexplore.ieee.org/document/9669030) |
| QMC（量子モンテカルロ） | [Quantum_Computing_Quantum_Monte_Carlo.ipynb](notebooks/advanced_algorithms/Quantum_Computing_Quantum_Monte_Carlo.ipynb) | [Motta2018](https://wires.onlinelibrary.wiley.com/doi/10.1002/wcms.1364), [Peruzzo2014](https://www.nature.com/articles/ncomms5213) |
| 適応的ショット割り当て | [2_Adaptive_Shot_Allocation.ipynb](notebooks/advanced_algorithms/adaptive_shot_allocation/2_Adaptive_Shot_Allocation.ipynb) | [Shlosberg2023](https://doi.org/10.22331/q-2023-01-26-906) |

### 補助機能

| 機能 | ノートブック |
| ----- | ----- |
| ランダム回路生成 | [Random_Circuit.ipynb](notebooks/auxiliary_functions/Random_Circuit.ipynb) |

---
## コミュニティリポジトリ

> :warning: **以下のプロジェクトはAmazon Braketが提供するものではありません。これらのプロジェクトの使用（該当するライセンスの遵守や特定の目的への適合性を含む）については、ユーザー自身の責任となります。**

Braketを使用した他のリポジトリでの量子アルゴリズム実装：

| アルゴリズム | リポジトリ | 参考文献 | 追加の依存関係 |
| ----- | ----- | ----- | ----- |
| 量子強化学習 | [quantum-computing-exploration-for-drug-discovery-on-aws](https://github.com/awslabs/quantum-computing-exploration-for-drug-discovery-on-aws) | [Learning Retrosynthetic Planning through Simulated Experience(2019)](https://pubs.acs.org/doi/10.1021/acscentsci.9b00055) | [dependencies](https://github.com/awslabs/quantum-computing-exploration-for-drug-discovery-on-aws/blob/main/source/src/notebook/healthcare-and-life-sciences/d-1-retrosynthetic-planning-quantum-reinforcement-learning/requirements.txt)

[comment]: <> (If you wish to highlight your implementation,  append the following content in a new line to the table above : | <Name> | <link to github repo> | <published reference> | <list of required packages on top of what is listed in amazon-braket-algorithm-library setup.py> |)

---
## <a name="install">インストール方法</a>

### 方法1: uv を使用する（推奨）

[uv](https://github.com/astral-sh/uv)は高速なPythonパッケージマネージャーです。

```bash
git clone https://github.com/amazon-braket/amazon-braket-algorithm-library.git
cd amazon-braket-algorithm-library
uv sync
```

テスト用の依存関係も含める場合：

```bash
uv sync --extra test
```

コマンドを実行する：

```bash
uv run python <your_script.py>
uv run pytest test/unit_tests
```

### 方法2: pip を使用する

```bash
git clone https://github.com/amazon-braket/amazon-braket-algorithm-library.git
cd amazon-braket-algorithm-library
pip install .
```

---
## AWS設定

### AWSプロファイルの設定

ノートブックをローカルのIDEで実行するには、まずAWSアカウントと連携するためのプロファイルを設定します。詳細は[AWS CLIの設定](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)を参照してください。

プロファイル作成後、以下のコマンドで`AWS_PROFILE`を設定し、以降のコマンドがAWSアカウントとリソースにアクセスできるようにします：

```bash
export AWS_PROFILE=YOUR_PROFILE_NAME
```

### Amazon Braketに必要なリソースの設定

Amazon Braketを初めて使用する場合は、[AWSコンソール](https://console.aws.amazon.com/braket/home)からサービスのオンボーディングと必要なリソースの作成を行ってください。

---
## サポート

### 問題とバグレポート

アルゴリズムライブラリの使用中にバグが発生したり問題に直面した場合は、[GitHubのissueトラッカー](https://github.com/amazon-braket/amazon-braket-algorithm-library/issues)に投稿してお知らせください。

その他の問題や一般的な質問については、[Quantum Computing Stack Exchange](https://quantumcomputing.stackexchange.com/questions/ask)で質問し、タグ「amazon-braket」を追加してください。

### フィードバックと機能リクエスト

Amazon Braketに関するフィードバックや実装してほしい機能がある場合は、ぜひお聞かせください。
[GitHub issues](https://github.com/amazon-braket/amazon-braket-algorithm-library/issues)がフィードバックと機能リクエストを収集するための推奨メカニズムです。他のユーザーも会話に参加でき、+1で優先度を示すことができます。

---
## ライセンス

このプロジェクトはApache-2.0ライセンスの下でライセンスされています。
