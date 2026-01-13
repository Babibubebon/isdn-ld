# Linked Data for ISDN

[ISDN (International Standard Dojin Numbering)](https://isdn.jp/) の書誌情報を Linked Data (RDFデータセット) に変換する。

## Usage

### Install

```shell
pip install isdn-ld
```

### Convert

事前準備: [ISDN-Python](https://github.com/Babibubebon/isdn-python) で書誌情報XMLファイルをダウンロードしておく。

```shell
isdnld convert /path/to/xml_files/ /path/to/output/isdnld.nq
```

## Schema

[isdn.jp](https://isdn.jp/) が提供する書誌情報の XML Schema: <https://isdn.jp/schemas/0.1/isdn.xsd>

このXMLから少し意味的に理解を加えて設計した RDF モデルへマッピングしている。

### Graph URIs

quads形式で変換すると、コンテンツのレーティングに応じてグラフURIを分ける。

- `https://metadata.moe/isdn/graph/ageUnrestricted` : 一般
- `https://metadata.moe/isdn/graph/ageRestricted15` : 15禁
- `https://metadata.moe/isdn/graph/ageRestricted18` : 18禁

### Resource URI

`https://metadata.moe/isdn/res/{ISDN}`

### Vocabulary

WIP
