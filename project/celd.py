
class Celd(object):

    def __init__(self, y, x):
        self.content = 0
        self.y = y
        self.x = x
        self.visible = False
        self.flag = False
        self.question = False

    def __repr__(self):
        return "{}".format(self.content)

    def put_number(self, number):
        self.content = number

    def put_bomb(self):
        self.content = 9

    def is_bomb(self):
        bool = False
        if self.content == 9:
            bool = True

        return bool

    def show_content(self):
        self.visible = True
        return self.content

    def right_click_action(self):
        if not self.visible:
            if not self.flag and not self.question:
                self.flag = True

            elif self.flag and not self.question:
                self.flag = False
                self.question = True

            elif not self.flag and self.question:
                self.question = False

        return self.status_celd()

    def status_celd(self):
        status = "Visible"

        if not self.visible:
            if not self.flag and not self.question:
                status = "Invisible"

            elif self.flag and not self.question:
                status = "Flag"

            elif not self.flag and self.question:
                status = "Question"

        return status

    """def get_content(self):
        content_to_show = "empty"

        if not self.visible:
            if self.flag:
                content_to_show = "flag"
            elif self.question:
                content_to_show = "question"
        else:
            content_to_show = self.content

        return content_to_show"""
