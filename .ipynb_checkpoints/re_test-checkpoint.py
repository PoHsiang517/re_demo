{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "\n",
    "text = input(\"請輸入文字: \")\n",
    "\n",
    "re_comp = re.compile(r\"(魔術|文鳥|十姊妹|市場)\")\n",
    "re_list = re_comp.findall(text)\n",
    "\n",
    "for i in range(len(re_list)):\n",
    "    print(i)\n",
    "    i += 1"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
