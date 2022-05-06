import tkinter as tk
import numexpr as ne


class Calculator(tk.Tk):
    window_width = 423  # 320
    window_height = 310  # 422
    window_offset_x = 800
    window_offset_y = 300
    action_list = ["+", "-", "*", "/"]

    button_pady = 0  # 5 | 4.2
    button_padx = 5  # 3
    button_width = 3  # 4 | 3
    button_height = 1  # 3 | 2
    buttons_background = "grey88"
    buttons_font = "Arial 20"
    buttons_boreground = 1.5  # 1.5
    specific_button_pady = 5.3  # 0 | 5.3
    specific_button_padx = 5  # 1
    specific_button_width = 3  # 4 | 3
    specific_button_height = 1  # 2 | 1

    text_label_height = 3

    def __init__(self):
        super().__init__()

        self.buttons_frame = tk.Frame(self)
        # self.buttons_action_frame = tk.Frame(self.buttons_frame)
        self.text_label = tk.Label(self)

        self.button_0 = tk.Button(self.buttons_frame)
        self.button_1 = tk.Button(self.buttons_frame)
        self.button_2 = tk.Button(self.buttons_frame)
        self.button_3 = tk.Button(self.buttons_frame)
        self.button_4 = tk.Button(self.buttons_frame)
        self.button_5 = tk.Button(self.buttons_frame)
        self.button_6 = tk.Button(self.buttons_frame)
        self.button_7 = tk.Button(self.buttons_frame)
        self.button_8 = tk.Button(self.buttons_frame)
        self.button_9 = tk.Button(self.buttons_frame)
        self.button_equal = tk.Button(self.buttons_frame)
        self.button_comma = tk.Button(self.buttons_frame)
        self.button_plus = tk.Button(self.buttons_frame)
        self.button_minus = tk.Button(self.buttons_frame)
        self.button_multiply = tk.Button(self.buttons_frame)
        self.button_divide = tk.Button(self.buttons_frame)
        self.button_clear_all = tk.Button(self.buttons_frame)
        self.button_backspace = tk.Button(self.buttons_frame)
        self.button_bracket_open = tk.Button(self.buttons_frame)
        self.button_bracket_close = tk.Button(self.buttons_frame)

        self.init_ui()

    def init_ui(self):
        self.title("Calcularium")
        self.resizable(width=False, height=False)
        self.geometry(
            f"{Calculator.window_width}x{Calculator.window_height}+{Calculator.window_offset_x}+{Calculator.window_offset_y}")

        self.text_label.configure(height=Calculator.text_label_height, anchor='e', font="Arial 18", bg="grey88",
                                  text="0")
        self.button_0.configure(width=Calculator.button_width, height=Calculator.button_height, text="0",
                                bg=Calculator.buttons_background, font=Calculator.buttons_font,
                                bd=Calculator.buttons_boreground)
        self.button_1.configure(width=Calculator.button_width, height=Calculator.button_height, text="1",
                                bg=Calculator.buttons_background, font=Calculator.buttons_font,
                                bd=Calculator.buttons_boreground)
        self.button_2.configure(width=Calculator.button_width, height=Calculator.button_height, text="2",
                                bg=Calculator.buttons_background, font=Calculator.buttons_font,
                                bd=Calculator.buttons_boreground)
        self.button_3.configure(width=Calculator.button_width, height=Calculator.button_height, text="3",
                                bg=Calculator.buttons_background, font=Calculator.buttons_font,
                                bd=Calculator.buttons_boreground)
        self.button_4.configure(width=Calculator.button_width, height=Calculator.button_height, text="4",
                                bg=Calculator.buttons_background, font=Calculator.buttons_font,
                                bd=Calculator.buttons_boreground)
        self.button_5.configure(width=Calculator.button_width, height=Calculator.button_height, text="5",
                                bg=Calculator.buttons_background, font=Calculator.buttons_font,
                                bd=Calculator.buttons_boreground)
        self.button_6.configure(width=Calculator.button_width, height=Calculator.button_height, text="6",
                                bg=Calculator.buttons_background, font=Calculator.buttons_font,
                                bd=Calculator.buttons_boreground)
        self.button_7.configure(width=Calculator.button_width, height=Calculator.button_height, text="7",
                                bg=Calculator.buttons_background, font=Calculator.buttons_font,
                                bd=Calculator.buttons_boreground)
        self.button_8.configure(width=Calculator.button_width, height=Calculator.button_height, text="8",
                                bg=Calculator.buttons_background, font=Calculator.buttons_font,
                                bd=Calculator.buttons_boreground)
        self.button_9.configure(width=Calculator.button_width, height=Calculator.button_height, text="9",
                                bg=Calculator.buttons_background, font=Calculator.buttons_font,
                                bd=Calculator.buttons_boreground)
        self.button_equal.configure(width=Calculator.button_width, height=Calculator.button_height, text="=",
                                    bg=Calculator.buttons_background, font=Calculator.buttons_font,
                                    bd=Calculator.buttons_boreground)
        self.button_comma.configure(width=Calculator.button_width, height=Calculator.button_height, text=".",
                                    bg=Calculator.buttons_background, font=Calculator.buttons_font,
                                    bd=Calculator.buttons_boreground)
        self.button_plus.configure(width=Calculator.specific_button_width, height=Calculator.specific_button_height,
                                   text="+", bg=Calculator.buttons_background, font=Calculator.buttons_font,
                                   bd=Calculator.buttons_boreground)
        self.button_minus.configure(width=Calculator.specific_button_width, height=Calculator.specific_button_height,
                                    text="-", bg=Calculator.buttons_background, font=Calculator.buttons_font,
                                    bd=Calculator.buttons_boreground)
        self.button_multiply.configure(width=Calculator.specific_button_width, height=Calculator.specific_button_height,
                                       text="*", bg=Calculator.buttons_background, font=Calculator.buttons_font,
                                       bd=Calculator.buttons_boreground)
        self.button_divide.configure(width=Calculator.specific_button_width, height=Calculator.specific_button_height,
                                     text="/", bg=Calculator.buttons_background, font=Calculator.buttons_font,
                                     bd=Calculator.buttons_boreground)
        self.button_backspace.configure(width=Calculator.specific_button_width,
                                        height=Calculator.specific_button_height, text="<-",
                                        bg=Calculator.buttons_background, font=Calculator.buttons_font,
                                        bd=Calculator.buttons_boreground)
        self.button_clear_all.configure(width=Calculator.specific_button_width,
                                        height=Calculator.specific_button_height, text="Clear",
                                        bg=Calculator.buttons_background, font=Calculator.buttons_font,
                                        bd=Calculator.buttons_boreground)
        self.button_bracket_open.configure(width=Calculator.specific_button_width,
                                           height=Calculator.specific_button_height, text="(",
                                           bg=Calculator.buttons_background, font=Calculator.buttons_font,
                                           bd=Calculator.buttons_boreground)
        self.button_bracket_close.configure(width=Calculator.specific_button_width,
                                            height=Calculator.specific_button_height, text=")",
                                            bg=Calculator.buttons_background, font=Calculator.buttons_font,
                                            bd=Calculator.buttons_boreground)

        self.button_0.bind("<Button-1>", self.insert_symbol)
        self.button_1.bind("<Button-1>", self.insert_symbol)
        self.button_2.bind("<Button-1>", self.insert_symbol)
        self.button_3.bind("<Button-1>", self.insert_symbol)
        self.button_4.bind("<Button-1>", self.insert_symbol)
        self.button_5.bind("<Button-1>", self.insert_symbol)
        self.button_6.bind("<Button-1>", self.insert_symbol)
        self.button_7.bind("<Button-1>", self.insert_symbol)
        self.button_8.bind("<Button-1>", self.insert_symbol)
        self.button_9.bind("<Button-1>", self.insert_symbol)
        self.button_equal.bind("<Button-1>", self.calc_and_insert_result)
        self.button_comma.bind("<Button-1>", self.insert_symbol)
        self.button_plus.bind("<Button-1>", self.insert_symbol)
        self.button_minus.bind("<Button-1>", self.insert_symbol)
        self.button_multiply.bind("<Button-1>", self.insert_symbol)
        self.button_divide.bind("<Button-1>", self.insert_symbol)
        self.button_clear_all.bind("<Button-1>", self.clear_all)
        self.button_backspace.bind("<Button-1>", self.backspace)
        self.button_bracket_open.bind("<Button-1>", self.insert_symbol)
        self.button_bracket_close.bind("<Button-1>", self.insert_symbol)

        self.bind("<KP_Enter>", self.calc_and_insert_result)
        self.bind("<BackSpace>", self.backspace)
        self.bind("<Shift-BackSpace>", self.clear_all)
        self.bind("<Key>", self.numpad_insert)
        self.bind("<Return>", self.calc_and_insert_result)

        self.text_label.pack(fill=tk.X, expand=0)
        self.buttons_frame.pack(fill=tk.BOTH, expand=1)
        self.button_0.grid(row=3, column=1, pady=Calculator.button_pady, padx=Calculator.button_padx)
        self.button_1.grid(row=0, column=0, pady=Calculator.button_pady, padx=Calculator.button_padx)
        self.button_2.grid(row=0, column=1, pady=Calculator.button_pady, padx=Calculator.button_padx)
        self.button_3.grid(row=0, column=2, pady=Calculator.button_pady, padx=Calculator.button_padx)
        self.button_4.grid(row=1, column=0, pady=Calculator.button_pady, padx=Calculator.button_padx)
        self.button_5.grid(row=1, column=1, pady=Calculator.button_pady, padx=Calculator.button_padx)
        self.button_6.grid(row=1, column=2, pady=Calculator.button_pady, padx=Calculator.button_padx)
        self.button_7.grid(row=2, column=0, pady=Calculator.button_pady, padx=Calculator.button_padx)
        self.button_8.grid(row=2, column=1, pady=Calculator.button_pady, padx=Calculator.button_padx)
        self.button_9.grid(row=2, column=2, pady=Calculator.button_pady, padx=Calculator.button_padx)
        self.button_equal.grid(row=3, column=2, pady=Calculator.button_pady, padx=Calculator.button_padx)
        self.button_comma.grid(row=3, column=0, pady=Calculator.button_pady, padx=Calculator.button_padx)

        # self.buttons_action_frame.grid(row=0, column=3, rowspan=10)
        self.button_multiply.grid(row=0, column=3, pady=Calculator.specific_button_pady,
                                  padx=Calculator.specific_button_padx)
        self.button_plus.grid(row=1, column=3, pady=Calculator.specific_button_pady,
                              padx=Calculator.specific_button_padx)
        self.button_minus.grid(row=2, column=3, pady=Calculator.specific_button_pady,
                               padx=Calculator.specific_button_padx)
        self.button_divide.grid(row=3, column=3, pady=Calculator.specific_button_pady,
                                padx=Calculator.specific_button_padx)
        self.button_clear_all.grid(row=0, column=4, pady=Calculator.specific_button_pady,
                                   padx=Calculator.specific_button_padx)
        self.button_backspace.grid(row=1, column=4, pady=Calculator.specific_button_pady,
                                   padx=Calculator.specific_button_padx)
        self.button_bracket_open.grid(row=2, column=4, pady=Calculator.specific_button_pady,
                                      padx=Calculator.specific_button_padx)
        self.button_bracket_close.grid(row=3, column=4, pady=Calculator.specific_button_pady,
                                       padx=Calculator.specific_button_padx)

    def backspace(self, event):
        self.text_label["text"] = self.text_label["text"][0:-1]

    def clear_all(self, event):
        self.text_label["text"] = "0"

    def numpad_insert(self, event):
        if event.keycode not in range(10, 20) and event.char not in Calculator.action_list and "KP" not in event.keysym:
            return

        try:
            if self.text_label["text"][0] == '0':
                self.text_label["text"] = self.text_label["text"][1:]

            if event.char in Calculator.action_list:
                if self.text_label["text"][-1] in Calculator.action_list:
                    self.text_label["text"] = self.text_label["text"][0:-1] + event.char
                    return
                self.text_label["text"] = self.text_label["text"][0:] + event.char
                return
        except IndexError:
            pass

        if event.char == ".":
            self.parse_string()
            return

        self.text_label["text"] += event.char

    def insert_symbol(self, event):
        try:
            if self.text_label["text"][0] == '0':
                self.text_label["text"] = self.text_label["text"][1:]

            if event.widget["text"] in Calculator.action_list:
                if self.text_label["text"][-1] in Calculator.action_list:
                    self.text_label["text"] = self.text_label["text"][0:-1] + event.widget["text"]
                    return
                self.text_label["text"] = self.text_label["text"][0:] + event.widget["text"]
                return
        except IndexError:
            pass

        if event.widget["text"] == ".":
            self.parse_string()
            return

        self.text_label["text"] += event.widget["text"]

    def parse_string(self):
        obj = self.text_label["text"]
        result = {}
        res_index = 0
        buf = []
        for letter in obj:
            if letter in Calculator.action_list:
                result[res_index] = buf
                res_index += 1
                result[res_index] = letter
                res_index += 1
                buf = []
                continue
            buf.append(letter)
        result[res_index + 1] = buf
        last_number = len(result)
        buf = result[last_number]
        if "." in buf:
            if buf[0] == "0":
                del buf[0]
            del buf[buf.index('.')]
            buf.append('.')
        else:
            buf.append('.')
        string_return = ""
        for key, val in result.items():
            string_return += "".join(val)
        print(result)
        print(string_return)
        self.text_label["text"] = string_return

    def calc_and_insert_result(self, event):
        try:
            self.text_label["text"] = str(ne.evaluate(self.text_label["text"]))
        except Exception:
            pass


def main():
    app = Calculator()
    app.mainloop()


if __name__ == '__main__':
    main()
