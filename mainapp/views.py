from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'Products',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00',
             'comment': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             'src': 'vendor/img/products/Adidas%20hoodie.png'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00',
             'comment': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             'src': 'vendor/img/products/Blue%20jacket%20The%20North%20Face.png'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00',
             'comment': 'Материал с плюшевой текстурой. Удобный и мягкий.',
             'src': 'vendor/img/products/Brown%20sports%20oversized-top%20ASOS%20DESIGN.png'},
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00',
             'comment': 'Плотная ткань. Легкий материал.',
             'src': 'vendor/img/products/Black%20Nike%20Heritage%20backpack.png'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00',
             'comment': 'Гладкий кожаный верх. Натуральный материал.Гладкий кожаный верх. Натуральный материал.',
             'src': 'vendor/img/products/Black%20Dr%20Martens%20shoes.png'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2 890,00',
             'comment': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
             'src': 'vendor/img/products/Dark%20blue%20wide-leg%20ASOs%20DESIGN%20trousers.png'},
        ],
    }
    return render(request, 'mainapp/products.html', context)
