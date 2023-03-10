import unittest

import social


class TestBlog(unittest.TestCase):

    def test_generate_blog(self):
        BLOG_RSS_LINK = "https://zylele.github.io/atom.xml"
        BLOG_LIMIT = 3

        old_readme = social.BLOG_START_COMMENT + "old_content" + social.BLOG_END_COMMENT
        new_readme = old_readme

        print("BLOG_RSS_LINK:" + BLOG_RSS_LINK)
        print("BLOG_LIMIT:" + str(BLOG_LIMIT))
        new_readme = social.generate_blog(BLOG_RSS_LINK, BLOG_LIMIT, new_readme)
        print("new_readme:")
        print(new_readme)
        self.assertNotEqual(old_readme, new_readme)


if __name__ == '__main__':
    unittest.main()
