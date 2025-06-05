# Kosen2023-Multi2STE

このリポジトリは、高専時代の卒業研究の備忘録として作成されたものです。
使用していた動画像データは肖像権に関わるため、非公開または一部削除されています。

## 📁 プロジェクト構成

* **A\_yolov7/**: YOLOv7を用いた2D姿勢推定モデル
* **B\_StridedTransformer-Pose3D/**: Strided Transformerを用いた3D姿勢推定モデル
* **C\_plot3d\_with\_html/**: 3D姿勢データのHTML可視化ツール
* **D\_JSON/**: 姿勢データなどの数値群解析用
* **Makefile**: ビルドや実行の自動化スクリプト
* **environment.yaml**: Anaconda環境設定ファイル

## 🛠️ 環境構築

1. Anaconda環境の作成

   ```bash
   conda env create -f environment.yaml
   conda activate py38Multi2STE
   ```

2. 必要なモデルファイルの配置

   `B_StridedTransformer-Pose3D/demo/lib/checkpoint/` に下記ファイルを配置してください:

   * `pose_hrnet_w48_384x288.pth`
   * `yolov3.weights`

   ※ これらのファイルはGitHubのファイルサイズ制限 (100MB) を超えるため、リポジトリには含まれていません。Git LFSの使用を検討してください。

## 🚀 使用方法

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

## ⚠️ 注意事項

* `A_yolov7/traced_model.pt` や `B_StridedTransformer-Pose3D/video/` などの一部ファイルは、サイズ制限や肖像権の関係でリポジトリには含まれていません。
* `.gitignore` ファイルを適切に設定し、不要なファイルがコミットされないようにしてください。

