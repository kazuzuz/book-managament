from book.models import Book

books_to_create = [

    {"title": "ドラゴンボール", "author": "鳥山明"},
    {"title": "ブリーチ", "author": "久保帯人"},
    {"title": "僕のヒーローアカデミア", "author": "堀越耕平"},
    {"title": "鬼滅の刃", "author": "吾峠呼世晴"},
    {"title": "ブラッククローバー", "author": "田畠裕基"},
]


Book.objects.bulk_create(books_to_create)
