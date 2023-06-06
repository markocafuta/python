class _UnbalancedBracesError(Exception):
    pass


class _BracesChecker:

    def __init__(self, text):
        self.__BRACES = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        self.__INVERSED_BRACES = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        self.__BALANCED_MESSAGE = "Braces are balanced."
        self.__stack = []
        self.__text = text

    def check_if_balanced(self):
        for i, char in enumerate(self.__text):
            if self.__is_open_brace(char):
                self.__append_close_brace_to_stack(char)
            elif self.__is_unbalanced(char):
                raise _UnbalancedBracesError(self.__unbalanced_text_till_index(i, char))

        return self.__get_balanced_message_if_stack_empty()

    def __get_balanced_message_if_stack_empty(self):
        if self.__is_stack_empty():
            return self.__BALANCED_MESSAGE
        else:
            raise _UnbalancedBracesError(self.__unbalanced_text())

    def __unbalanced_text_till_index(self, i, char):
        if not self.__is_stack_empty() and char == self.__pop_from_stack():
            index = i
        else:
            index = i + 1

        return self.__text[0:index]

    def __unbalanced_text(self):
        return self.__text[0:self.__get_last_unclosed_brace_index(self.__text)]

    def __is_open_brace(self, char):
        return self.__BRACES.get(char, False)

    def __is_closed_brace(self, char):
        return self.__INVERSED_BRACES.get(char, False)

    def __is_unbalanced(self, char):
        return self.__is_closed_brace(char) and (self.__is_stack_empty() or not char == self.__pop_from_stack())

    def __is_stack_empty(self):
        return len(self.__stack) == 0

    def __append_close_brace_to_stack(self, char):
        self.__stack.append(self.__BRACES[char])

    def __pop_from_stack(self):
        return self.__stack.pop()

    def __get_last_unclosed_brace_index(self, text):
        return text.rindex(self.__INVERSED_BRACES[self.__pop_from_stack()]) + 1
