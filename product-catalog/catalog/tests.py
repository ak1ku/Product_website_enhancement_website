from django.test import TestCase
from django.urls import reverse
from .models import Product, UserProfile, Cart, Wishlist, CartItem
from django.contrib.auth.models import User

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            pr_cate='Men',
            pr_name='Test Product',
            pr_price=29.99,
            pr_reviews=4.5,
            pr_buy_quant=10,
            pr_stk_quant=100,
            pr_images='product_images/test_image.jpg'
        )

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Test Product')

class UserProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = UserProfile.objects.create(user=self.user, phone='1234567890')

    def test_user_profile_str(self):
        self.assertEqual(str(self.profile), 'testuser')

class CartModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.cart = Cart.objects.create(user=self.user)

    def test_cart_str(self):
        self.assertEqual(str(self.cart), 'Cart of testuser')

class CartItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.product = Product.objects.create(
            pr_cate='Men',
            pr_name='Test Product',
            pr_price=29.99
        )
        self.cart = Cart.objects.create(user=self.user)
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)

    def test_cart_item_str(self):
        self.assertEqual(str(self.cart_item), '2 x Test Product')

class CartViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_cart_view(self):
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/cart.html')

class AddToCartViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.product = Product.objects.create(
            pr_cate='Men',
            pr_name='Test Product',
            pr_price=29.99
        )

    def test_add_to_cart(self):
        response = self.client.post(reverse('add_to_cart', args=[self.product.pr_id]), {'quantity': 1})
        self.assertEqual(response.status_code, 302)  # Redirect after adding to cart
        self.assertEqual(CartItem.objects.count(), 1)

    def test_add_to_cart_invalid_product(self):
        response = self.client.post(reverse('add_to_cart', args=[999]), {'quantity': 1})
        self.assertEqual(response.status_code, 404)  # Product not found

class WishlistViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.wishlist = Wishlist.objects.create(user=self.user)

    def test_wishlist_view(self):
        response = self.client.get(reverse('wishlist'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/wishlist.html')