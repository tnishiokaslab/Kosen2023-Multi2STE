# Kosen2023-Multi2STE

このリポジトリは、高等専門学校時代の卒業研究に基づいて作成された、研究活動の備忘録および再現用コードです。

本研究のテーマは、**複数人が映る動画における3D姿勢推定の高精度化と応用** です。  
従来の 3D 姿勢推定モデルは主に単一人物を対象として設計されていましたが、実社会での応用（スポーツ、医療、行動解析など）を考えると、**複数人を同時に処理できることが重要**です。

そこで本研究では、単一人物向けの 3D 姿勢推定モデルである **StridedTransformer** を、**YOLOv7** による人物検出・切り出しによって複数人動画へ適用可能とし、bottom-up 的に課題を解決するアプローチを取りました。

このような手法により、武道やスポーツにおける「型」などの高度な動作分析を可能とし、技術修練支援やフォーム評価への応用を目指しました。

当時指導いただいた教授、および撮影・研究にご協力いただいた少林寺拳法部の先生方・仲間たちに深く感謝申し上げます。

> 使用していた動画像データは肖像権の都合により、非公開または一部削除されています。
<p align="center">
  <div style="display: inline-block; text-align: center; margin-right: 20px;">
    <img src="img/yolov7.png" alt="人物検出 (Yolov7)" width="170"><br>
    <span><strong>人物検出 (Yolov7)</strong></span>
  </div>
  <div style="display: inline-block; text-align: center;">
    <img src="img/STE.png" alt="姿勢推定 (Strided Transformer)" width="200"><br>
    <span><strong>姿勢推定 (Strided Transformer)</strong></span>
  </div>
</p>


##  プロジェクト構成

* **A\_yolov7/**: YOLOv7を用いた2D姿勢推定モデル
* **B\_StridedTransformer-Pose3D/**: Strided Transformerを用いた3D姿勢推定モデル
* **C\_plot3d\_with\_html/**: 3D姿勢データのHTML可視化ツール
* **D\_JSON/**: 姿勢データなどの数値群解析用
* **Makefile**: ビルドや実行の自動化スクリプト
* **environment.yaml**: Anaconda環境設定ファイル

##  環境構築

1. Anaconda環境の作成

   ```bash
   conda env create -f environment.yaml
   conda activate py38Multi2STE
   ```

2. 必要なモデルファイルの配置

   `B_StridedTransformer-Pose3D/demo/lib/checkpoint/` に下記ファイルを配置してください:

   * `pose_hrnet_w48_384x288.pth`
   * `yolov3.weights`

   ※ これらのファイルはGitHubのファイルサイズ制限 (100MB) を超えるため、リポジトリには含まれていません。

##  使用方法

1. 2D姿勢推定

   ```bash
   cd A_yolov7
   python detect.py --source path_to_video
   ```

2. 3D姿勢推定

   ```bash
   cd ../B_StridedTransformer-Pose3D
   python run.py --input path_to_2d_keypoints
   ```

3. 3D可視化

   ```bash
   cd ../C_plot3d_with_html
   python visualize.py --input path_to_3d_keypoints
   ```


