# Alternative version to add tear down fixture
# @pytest.fixture(scope="module")
# def app(request):
#      fixture = Application()
#
#      def fin():
#          fixture.destroy()
#
#      request.addfinalizer(fin)
#      return fixture