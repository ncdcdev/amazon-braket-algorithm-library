"""
プロジェクト自動初期化スクリプト
Python起動時に自動的に.envファイルを読み込みます
"""
import os
import sys
from pathlib import Path


def load_project_env():
    """プロジェクトルートの.envファイルを読み込む"""
    # このファイルがプロジェクトルートにあると仮定
    project_root = Path(__file__).parent
    env_file = project_root / ".env"

    if env_file.exists():
        try:
            from dotenv import load_dotenv
            load_dotenv(env_file)

            # Jupyter環境でのみメッセージを表示
            if 'ipykernel' in sys.modules or 'IPython' in sys.modules:
                print(f"✓ 環境変数を読み込みました: .env")

                aws_profile = os.environ.get('AWS_PROFILE')
                if aws_profile:
                    print(f"  AWS_PROFILE: {aws_profile}")
        except ImportError:
            pass  # python-dotenvがない場合は何もしない
        except Exception:
            pass  # エラーは無視


def add_notebooks_to_path():
    """ノートブック用のヘルパーモジュールをPythonパスに追加"""
    project_root = Path(__file__).parent
    notebooks_textbook = project_root / "notebooks" / "textbook"

    if notebooks_textbook.exists() and str(notebooks_textbook) not in sys.path:
        sys.path.insert(0, str(notebooks_textbook))

        # Jupyter環境でのみメッセージを表示
        if 'ipykernel' in sys.modules or 'IPython' in sys.modules:
            print("✓ notebook_plottingを読み込み可能にしました")


# 自動実行
load_project_env()
add_notebooks_to_path()
