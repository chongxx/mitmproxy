import tutils

class TestApp(tutils.DaemonTests):
    SSL = False
    def test_index(self):
        r = self.getpath("/")
        assert r.status_code == 200
        assert r.content
        
    def test_docs(self):
        assert self.getpath("/docs/pathod").status_code == 200
        assert self.getpath("/docs/pathoc").status_code == 200
        assert self.getpath("/docs/language").status_code == 200
        assert self.getpath("/docs/test").status_code == 200

    def test_log(self):
        assert self.getpath("/log").status_code == 200
        assert self.get("200").status_code == 200
        id = self.d.log()[0]["id"]
        assert self.getpath("/log").status_code == 200
        assert self.getpath("/log/%s"%id).status_code == 200
        assert self.getpath("/log/9999999").status_code == 404
