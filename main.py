import tkinter as tk
import numexpr as ne


def parse_string(full_string: str, symbol: str) -> str:
    result = {}
    res_index = 0
    buf = []

    def bracket_parse() -> str:
        result_string = ""
        open_bracket_count = 0
        close_bracket_count = 0

        try:
            if symbol == '(':
                if full_string[-1] == '(':
                    result_string = full_string + symbol
                    return result_string

                if full_string[-1] == ')':
                    return full_string

                if full_string[-1] not in MainFrame.action_list and full_string[-1] not in Input.problem_symbols:
                    return full_string

            if symbol == ')':
                if full_string[-1] == '(':
                    return full_string

                if full_string[-1] == ')':
                    for letter in full_string:
                        if letter == '(':
                            open_bracket_count += 1
                        if letter == ')':
                            close_bracket_count += 1

                    if open_bracket_count > close_bracket_count:
                        result_string = full_string + symbol
                        return result_string

                    if open_bracket_count == close_bracket_count:
                        return full_string

                    if open_bracket_count == 0:
                        return full_string

                if full_string[-1] in MainFrame.action_list:
                    return full_string
        except IndexError:
            pass

        result_string = full_string + symbol
        return result_string

    if symbol == '(' or symbol == ')':
        return bracket_parse()

    for letter in full_string:
        if letter in MainFrame.action_list:
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

    if symbol in buf:
        if buf[0] == "0":
            del buf[0]
        del buf[buf.index(symbol)]
        buf.append(symbol)
    else:
        buf.append(symbol)

    string_return = ""

    for key, val in result.items():
        string_return += "".join(val)

    return string_return


class Input:
    problem_symbols = [".", "(", ")"]

    def __init__(self, input_field: tk.Label):
        self.input_field = input_field

    def backspace(self, event):
        self.input_field["text"] = self.input_field["text"][0:-1]

    def clear_all(self, event):
        self.input_field["text"] = "0"

    def calc_and_insert_result(self, event):
        try:
            self.input_field["text"] = str(ne.evaluate(self.input_field["text"]))
        except Exception:
            pass


class KeyboardInput(Input):
    keyboard_index_of_1 = 10
    keyboard_index_of_0 = 20

    def insert_symbol(self, event):
        if event.keycode not in range(KeyboardInput.keyboard_index_of_1,
                                      KeyboardInput.keyboard_index_of_0) and event.char not in MainFrame.action_list and "KP" not in event.keysym:
            return

        try:
            if self.input_field["text"][0] == '0':
                self.input_field["text"] = self.input_field["text"][1:]

            if event.char in MainFrame.action_list:
                if self.input_field["text"][-1] in MainFrame.action_list:
                    self.input_field["text"] = self.input_field["text"][0:-1] + event.char
                    return
                self.input_field["text"] = self.input_field["text"][0:] + event.char
                return
        except IndexError:
            pass

        if event.char in Input.problem_symbols:
            self.input_field["text"] = parse_string(self.input_field["text"], event.char)
            return

        self.input_field["text"] += event.char


class ButtonInput(Input):
    def insert_symbol(self, event):
        try:
            if self.input_field["text"][0] == '0':
                self.input_field["text"] = self.input_field["text"][1:]

            if event.widget["text"] in MainFrame.action_list:
                if self.input_field["text"][-1] in MainFrame.action_list:
                    self.input_field["text"] = self.input_field["text"][0:-1] + event.widget["text"]
                    return
                self.input_field["text"] = self.input_field["text"][0:] + event.widget["text"]
                return
        except IndexError:
            pass

        if event.widget["text"] in Input.problem_symbols:
            self.input_field["text"] = parse_string(self.input_field["text"], event.widget["text"])
            return

        self.input_field["text"] += event.widget["text"]


class InputInterface:
    def __init__(self, input_field: tk.Label):
        self.buttons = ButtonInput(input_field)
        self.keyboard = KeyboardInput(input_field)
        self.input = Input(input_field)


class MainFrame(tk.Frame):
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

    text_label_height = 3  # 3

    def __init__(self, master: tk.Tk):
        super().__init__(master=master)

        self.master = master
        self.buttons_frame = tk.Frame(self)
        self.text_label = tk.Label(self)
        self.input = InputInterface(self.text_label)

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
        self.init_logic()

    def init_ui(self):
        self.text_label.configure(height=MainFrame.text_label_height, anchor='e', font="Arial 18", bg="grey88",
                                  text="0")
        self.button_0.configure(width=MainFrame.button_width, height=MainFrame.button_height, text="0",
                                bg=MainFrame.buttons_background, font=MainFrame.buttons_font,
                                bd=MainFrame.buttons_boreground)
        self.button_1.configure(width=MainFrame.button_width, height=MainFrame.button_height, text="1",
                                bg=MainFrame.buttons_background, font=MainFrame.buttons_font,
                                bd=MainFrame.buttons_boreground)
        self.button_2.configure(width=MainFrame.button_width, height=MainFrame.button_height, text="2",
                                bg=MainFrame.buttons_background, font=MainFrame.buttons_font,
                                bd=MainFrame.buttons_boreground)
        self.button_3.configure(width=MainFrame.button_width, height=MainFrame.button_height, text="3",
                                bg=MainFrame.buttons_background, font=MainFrame.buttons_font,
                                bd=MainFrame.buttons_boreground)
        self.button_4.configure(width=MainFrame.button_width, height=MainFrame.button_height, text="4",
                                bg=MainFrame.buttons_background, font=MainFrame.buttons_font,
                                bd=MainFrame.buttons_boreground)
        self.button_5.configure(width=MainFrame.button_width, height=MainFrame.button_height, text="5",
                                bg=MainFrame.buttons_background, font=MainFrame.buttons_font,
                                bd=MainFrame.buttons_boreground)
        self.button_6.configure(width=MainFrame.button_width, height=MainFrame.button_height, text="6",
                                bg=MainFrame.buttons_background, font=MainFrame.buttons_font,
                                bd=MainFrame.buttons_boreground)
        self.button_7.configure(width=MainFrame.button_width, height=MainFrame.button_height, text="7",
                                bg=MainFrame.buttons_background, font=MainFrame.buttons_font,
                                bd=MainFrame.buttons_boreground)
        self.button_8.configure(width=MainFrame.button_width, height=MainFrame.button_height, text="8",
                                bg=MainFrame.buttons_background, font=MainFrame.buttons_font,
                                bd=MainFrame.buttons_boreground)
        self.button_9.configure(width=MainFrame.button_width, height=MainFrame.button_height, text="9",
                                bg=MainFrame.buttons_background, font=MainFrame.buttons_font,
                                bd=MainFrame.buttons_boreground)
        self.button_equal.configure(width=MainFrame.button_width, height=MainFrame.button_height, text="=",
                                    bg=MainFrame.buttons_background, font=MainFrame.buttons_font,
                                    bd=MainFrame.buttons_boreground)
        self.button_comma.configure(width=MainFrame.button_width, height=MainFrame.button_height, text=".",
                                    bg=MainFrame.buttons_background, font=MainFrame.buttons_font,
                                    bd=MainFrame.buttons_boreground)
        self.button_plus.configure(width=MainFrame.specific_button_width, height=MainFrame.specific_button_height,
                                   text="+", bg=MainFrame.buttons_background, font=MainFrame.buttons_font,
                                   bd=MainFrame.buttons_boreground)
        self.button_minus.configure(width=MainFrame.specific_button_width, height=MainFrame.specific_button_height,
                                    text="-", bg=MainFrame.buttons_background, font=MainFrame.buttons_font,
                                    bd=MainFrame.buttons_boreground)
        self.button_multiply.configure(width=MainFrame.specific_button_width, height=MainFrame.specific_button_height,
                                       text="*", bg=MainFrame.buttons_background, font=MainFrame.buttons_font,
                                       bd=MainFrame.buttons_boreground)
        self.button_divide.configure(width=MainFrame.specific_button_width, height=MainFrame.specific_button_height,
                                     text="/", bg=MainFrame.buttons_background, font=MainFrame.buttons_font,
                                     bd=MainFrame.buttons_boreground)
        self.button_backspace.configure(width=MainFrame.specific_button_width,
                                        height=MainFrame.specific_button_height, text="<-",
                                        bg=MainFrame.buttons_background, font=MainFrame.buttons_font,
                                        bd=MainFrame.buttons_boreground)
        self.button_clear_all.configure(width=MainFrame.specific_button_width,
                                        height=MainFrame.specific_button_height, text="Clear",
                                        bg=MainFrame.buttons_background, font=MainFrame.buttons_font,
                                        bd=MainFrame.buttons_boreground)
        self.button_bracket_open.configure(width=MainFrame.specific_button_width,
                                           height=MainFrame.specific_button_height, text="(",
                                           bg=MainFrame.buttons_background, font=MainFrame.buttons_font,
                                           bd=MainFrame.buttons_boreground)
        self.button_bracket_close.configure(width=MainFrame.specific_button_width,
                                            height=MainFrame.specific_button_height, text=")",
                                            bg=MainFrame.buttons_background, font=MainFrame.buttons_font,
                                            bd=MainFrame.buttons_boreground)

        self.text_label.pack(fill=tk.X, expand=0)
        self.buttons_frame.pack(fill=tk.BOTH, expand=1)
        self.button_0.grid(row=3, column=1, pady=MainFrame.button_pady, padx=MainFrame.button_padx)
        self.button_1.grid(row=0, column=0, pady=MainFrame.button_pady, padx=MainFrame.button_padx)
        self.button_2.grid(row=0, column=1, pady=MainFrame.button_pady, padx=MainFrame.button_padx)
        self.button_3.grid(row=0, column=2, pady=MainFrame.button_pady, padx=MainFrame.button_padx)
        self.button_4.grid(row=1, column=0, pady=MainFrame.button_pady, padx=MainFrame.button_padx)
        self.button_5.grid(row=1, column=1, pady=MainFrame.button_pady, padx=MainFrame.button_padx)
        self.button_6.grid(row=1, column=2, pady=MainFrame.button_pady, padx=MainFrame.button_padx)
        self.button_7.grid(row=2, column=0, pady=MainFrame.button_pady, padx=MainFrame.button_padx)
        self.button_8.grid(row=2, column=1, pady=MainFrame.button_pady, padx=MainFrame.button_padx)
        self.button_9.grid(row=2, column=2, pady=MainFrame.button_pady, padx=MainFrame.button_padx)
        self.button_equal.grid(row=3, column=2, pady=MainFrame.button_pady, padx=MainFrame.button_padx)
        self.button_comma.grid(row=3, column=0, pady=MainFrame.button_pady, padx=MainFrame.button_padx)

        self.button_multiply.grid(row=0, column=3, pady=MainFrame.specific_button_pady,
                                  padx=MainFrame.specific_button_padx)
        self.button_plus.grid(row=1, column=3, pady=MainFrame.specific_button_pady,
                              padx=MainFrame.specific_button_padx)
        self.button_minus.grid(row=2, column=3, pady=MainFrame.specific_button_pady,
                               padx=MainFrame.specific_button_padx)
        self.button_divide.grid(row=3, column=3, pady=MainFrame.specific_button_pady,
                                padx=MainFrame.specific_button_padx)
        self.button_clear_all.grid(row=0, column=4, pady=MainFrame.specific_button_pady,
                                   padx=MainFrame.specific_button_padx)
        self.button_backspace.grid(row=1, column=4, pady=MainFrame.specific_button_pady,
                                   padx=MainFrame.specific_button_padx)
        self.button_bracket_open.grid(row=2, column=4, pady=MainFrame.specific_button_pady,
                                      padx=MainFrame.specific_button_padx)
        self.button_bracket_close.grid(row=3, column=4, pady=MainFrame.specific_button_pady,
                                       padx=MainFrame.specific_button_padx)
        self.pack()

    def init_logic(self):
        self.button_0.bind("<Button-1>", self.input.buttons.insert_symbol)
        self.button_1.bind("<Button-1>", self.input.buttons.insert_symbol)
        self.button_2.bind("<Button-1>", self.input.buttons.insert_symbol)
        self.button_3.bind("<Button-1>", self.input.buttons.insert_symbol)
        self.button_4.bind("<Button-1>", self.input.buttons.insert_symbol)
        self.button_5.bind("<Button-1>", self.input.buttons.insert_symbol)
        self.button_6.bind("<Button-1>", self.input.buttons.insert_symbol)
        self.button_7.bind("<Button-1>", self.input.buttons.insert_symbol)
        self.button_8.bind("<Button-1>", self.input.buttons.insert_symbol)
        self.button_9.bind("<Button-1>", self.input.buttons.insert_symbol)
        self.button_equal.bind("<Button-1>", self.input.input.calc_and_insert_result)
        self.button_comma.bind("<Button-1>", self.input.buttons.insert_symbol)
        self.button_plus.bind("<Button-1>", self.input.buttons.insert_symbol)
        self.button_minus.bind("<Button-1>", self.input.buttons.insert_symbol)
        self.button_multiply.bind("<Button-1>", self.input.buttons.insert_symbol)
        self.button_divide.bind("<Button-1>", self.input.buttons.insert_symbol)
        self.button_clear_all.bind("<Button-1>", self.input.input.clear_all)
        self.button_backspace.bind("<Button-1>", self.input.input.backspace)
        self.button_bracket_open.bind("<Button-1>", self.input.buttons.insert_symbol)
        self.button_bracket_close.bind("<Button-1>", self.input.buttons.insert_symbol)

        self.master.bind("<KP_Enter>", self.input.input.calc_and_insert_result)
        self.master.bind("<BackSpace>", self.input.input.backspace)
        self.master.bind("<Shift-BackSpace>", self.input.input.clear_all)
        self.master.bind("<Key>", self.input.keyboard.insert_symbol)
        self.master.bind("<Return>", self.input.input.calc_and_insert_result)


class Calculator(tk.Tk):
    window_width = 423  # 320
    window_height = 310  # 422
    window_offset_x = 800
    window_offset_y = 300

    def __init__(self):
        super().__init__()
        self.main_frame = MainFrame(self)
        self.init_ui()

    def init_ui(self):
        self.title("Calcularium")
        self.resizable(width=False, height=False)
        self.geometry(
            f"{Calculator.window_width}x{Calculator.window_height}+{Calculator.window_offset_x}+{Calculator.window_offset_y}")


def main() -> None:
    app = Calculator()
    app.mainloop()


if __name__ == '__main__':
    main()
