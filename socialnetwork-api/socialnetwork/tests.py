from django.test import TestCase, Client
from django.urls import reverse


class APITest(TestCase):

    fixtures = ['my_db_test.json']

    def setUp(self):
        self.client = Client()
        self.token = self.get_token()

    '''
        endpoint token
    '''

    def get_token(self):
        data = {"username": 'Ervin',"password": 'admin@123'}
        url = reverse('api-token')
        response = self.client.post(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        print("\n> GET_TOKEN \nname: {}\nstatus_code: {}\nToken: {}".format(
        response.data['name'], response.status_code, response.data['token']))
        return 'Token ' + response.data['token']

    '''
        endpoints lists
    '''

    def test_user_list(self):
        url = reverse('users-list')
        response = self.client.get(url, HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 200)
        print("\n> TEST_USER_LIST \nstatus_code: {}".format(
        response.status_code))

    def test_profile_list(self):
        url = reverse('profiles-list')
        response = self.client.get(url, HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 200)
        print("\n> TEST_PROFILE_LIST \nstatus_code: {}".format(
        response.status_code))

    def test_post_list(self):
        url = reverse('posts-list')
        response = self.client.get(url, HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 200)
        print("\n> TEST_POST_LIST \nstatus_code: {}".format(
        response.status_code))

    def test_comment_list(self):
        url = reverse('comments-list')
        response = self.client.get(url, HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 200)
        print("\n> TEST_COMMENT_LIST \nstatus_code: {}".format(
        response.status_code))

    '''
        endpoints detail list
    '''

    def test_profile_detail(self):
        url = reverse('profile-detail', kwargs={'pk': 1})
        response = self.client.get(url, HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 200)
        print("\n> TEST_PROFILE_DETAIL \nname: {}\nstatus_code: {}".format(
        response.data['name'], response.status_code))

    def test_post_detail(self):
        url = reverse('post-detail', kwargs={'pk': 1})
        response = self.client.get(url, HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 200)
        print("\n> TEST_POST_DETAIL \nname: {}\nstatus_code: {}".format(
        response.data['name'], response.status_code))

    def test_comment_detail(self):
        url = reverse('comment-detail', kwargs={'pk_post': 1, 'pk_comment': 1})
        response = self.client.get(url, HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 200)
        print("\n> TEST_COMMENT_DETAIL \nname: {}\nstatus_code: {}".format(
        response.data['name'], response.status_code))

    '''
        endpoints detail update
    '''
    
    def test_profile_detail_update(self):
        data= {
            "name": "Naruto Uchiha",
            "email": "naruto@gmail.com",
            "address": {
                "street": "amaterasu",
                "suite": "Oca. 556",
                "city": "Konoha",
                "zipcode": "9256-7456"
            }
        }
        url = reverse('profile-detail', kwargs={'pk': 1})
        response = self.client.put(url, 
        data=data, content_type='application/json', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 200)
        print("\n> TEST_COMMENT_DETAIL_UPDATE \nname: {}\nstatus_code: {}".format(
        response.data['name'], response.status_code))

    def test_post_detail_update(self):
        data= {
            "title": "SOU PROPRIETARIO E CONSIGO EDITAR",
            "body": "Meu primeiro post modificado"
        }
        url = reverse('post-detail', kwargs={'pk': 11})
        response = self.client.put(url, 
        data=data, content_type='application/json', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 200)
        print("\n> TEST_POST_DETAIL_UPDATE \nuserId: {}\nstatus_code: {}".format(
        response.data['userId'], response.status_code))

    def test_comment_detail_update(self):
        data = {
            "name": "NELSON DIAS DE MEDEIROS",
            "email": "nelson@gmail.com",
            "body": "DEUS SEJA LOUVADO, ALELUIAAAAAA"
        }
        url = reverse('comment-detail', kwargs={'pk_post': 11, 'pk_comment': 52})
        response = self.client.put(url, 
        data=data, content_type='application/json', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 200)
        print("\n> TEST_COMMENT_DETAIL_UPDATE \nname: {}\nstatus_code: {}".format(
        response.data['name'], response.status_code))
    
    '''
        endpoints detail delete
    '''

    def test_profile_detail_delete(self):
        url = reverse('profile-detail', kwargs={'pk': 1})
        response = self.client.delete(url, HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 200)
        print("\n> TEST_PROFILE_DETAIL_DELETE \nstatus_code: {}".format(response.status_code))

    def test_post_detail_delete(self):
        url = reverse('post-detail', kwargs={'pk': 11})
        response = self.client.delete(url, HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 200)
        print("\n> TEST_POST_DETAIL_DELETE \nstatus_code: {}".format(response.status_code))
    
    def test_comment_detail_delete(self):
        url = reverse('comment-detail',  kwargs={'pk_post': 11, 'pk_comment': 52})
        response = self.client.delete(url, HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 200)
        print("\n> TEST_COMMENT_DETAIL_DELETE \nstatus_code: {}".format(response.status_code))

    '''
        test de permissões
    '''

    def test_post_detail_update_permission(self):
        data= {
            "title": "SOU PROPRIETARIO E CONSIGO EDITAR",
            "body": "Meu primeiro post modificado"
        }
        url = reverse('post-detail', kwargs={'pk': 1})
        response = self.client.put(url, 
        data=data, content_type='application/json', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 403)
        print("\n> TEST_POST_DETAIL_UPDATE_PERMISSIONS \nstatus_code: {}\nnotice: {}".format(
        response.status_code, response.data['detail']))

    def test_post_detail_delete_permission(self):
        url = reverse('post-detail', kwargs={'pk': 1})
        response = self.client.delete(url, HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 403)
        print("\n> TEST_POST_DETAIL_DELETE_PERMISSIONS \nstatus_code: {}\nnotice: {}".format(
        response.status_code, response.data['detail']))