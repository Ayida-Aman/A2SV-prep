# problem link: https://leetcode.com/problems/reverse-prefix-of-word/description/

class Solution(object):
    def reversePrefix(self, word, ch):
        wordList = list(word)
        if ch in wordList:
            index = wordList.index(ch)
            newWord=[]
            for i in range(index+1):
                newWord.append(wordList[i])

            for i in range(len(newWord)):
                wordList[i] = newWord.pop()
            return "".join(wordList)

        return word
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        