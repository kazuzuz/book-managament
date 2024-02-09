FROM python:3.8

#シェルを指定
SHELL ["/bin/bash", "-c"]

#コンテナ内で使用するディレクトリを指定
WORKDIR /bookmanagement

#ソフトウェアアップデート
RUN ["apt-get", "update"]

#PC上の「requirements.txt」を、WORKDIR上にコピー
COPY requirements.txt ./

#pipインストールの実行
RUN ["pip3", "install", "--no-cache-dir", "-r", "/bookmanagement/requirements.txt"]

#build中に確認できるように表示
RUN pip freeze

#PC上のsrcファイルをWORKDIR内にコピー
COPY . . 

#コンテナのポート8000を公開
EXPOSE 5000

#dockerコンテナ起動時に実行するコマンド
CMD ["manage.py", "runserver", "0.0.0.0:8000"]