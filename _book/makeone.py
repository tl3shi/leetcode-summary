#coding=utf-8
import os

#run in *nix/mac the new line for input file is mac
def parsefile(filename):
    f = open(filename)
    lines = f.readlines()
    result=[]
    needchange = False
    for i in range(10, len(lines)):
        line = lines[i]
        if (line.startswith("###")):
            if(len(lines[i-1]) >= 2):
                result.append('\n')
            line = line[:3] + ' ' + line[4:].strip()
            if(line[4] >= '0' and line[4] <= '5'):
                line = line[:4] + line[5:].strip()
                if(line[4] == '.'):
                    line = line[:4]+line[5:]
            line += '\n'
        if (line.startswith('```cpp')) and (len(lines[i-1]) > 2):
            needchange = True
            result.append('\n')
        result.append(line)
        if (line.startswith("###") and len(lines[i+1]) >= 2):
            result.append('\n')
    result.append('\n')
    f.close()
    if(needchange):
        output = open(filename, 'w')
        output.writelines(lines[:10])
        output.writelines(result)
        output.close()
    return result

def parseAll(filename):
    f = open(filename)
    lines = f.readlines()
    result=[]
    chapter=''
    i = 0
    for line in lines[9:]:
        if(line.startswith('###')):
            line = line[4:]
            chapter=line.split(',')[0]
        if(line.find('题解') == -1):
            result.append(line)
            continue
        s = line.find('(./')   
        e = line.find('.html')
        title = line[s+3:e]
        onefile = title +'.md'
        title = ' '.join(title.split('-'))
        #print title, onefile; exit();    
        if (onefile == 'Pow(x,-n).md'):
            onefile = 'powx-n.md'
        elif (onefile == 'Sqrt(x).md'):
            onefile = 'sqrtx.md'
        elif (onefile == 'String-to-Integer-(atoi).md'):
            onefile = 'string-to-integer-atoi.md'
        elif (onefile == 'Implement-strStr().md'):
            onefile = 'implement-strstr.md'
        elif (onefile == "Pascal's-Triangle.md"):
            onefile = 'pascals-triangle.md'
        elif (onefile == "Pascal's-Triangle-II.md"):
            onefile = 'pascals-triangle-ii.md'
        onefilecontent = parsefile(onefile)
        newfile=[]
        newfile.append('# ' + title + '\n\n')
        newfile += onefilecontent
        if not os.path.exists(chapter):
            os.makedirs(chapter)
        output = open(chapter+'/'+onefile, 'w+')
        output.writelines(newfile)
        output.close()

parseAll('leetcode-summary.md')
#parsefile('decode-ways.md')
#parsefile('add-two-numbers.md')
