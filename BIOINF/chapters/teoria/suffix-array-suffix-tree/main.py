#!/usr/bin/env python3
import os

class SuffixTreeNode:
    def __init__(self, value=None, children=[], label = None):
        self.value = value
        self.children = children
        self.label = label
    
    def __str__(self):
        value = "{}"
        if self.value:
            value = str(self.value)
        if self.label:
            value += f", label = {self.label}"

        children = []
        for child in self.children:
            children.append(str(child))
        
        children = "\n".join(children)
        return f"[ {value} {children} ]"
    
    def isLeaf(self):
        return len(self.children) == 0

class SuffixTree:
    def __init__(self, root = None):
        if not root:
            root = Node()
        self.root = root
    
    def __str__(self):
        return (
            "\\begin{forest}" + "\n" +
            "for tree={circle, black, draw, fill=blue!30, s sep=17mm}" + "\n" +
            str(self.root) + "\n" +
            "\\end{forest}" + "\n"
        )

class ForestDocument:
    def __init__(self, forests):
        self.forests = forests
    
    def __str__(self):
        return (
            "\\documentclass{article}" + "\n" +
            "\\usepackage{forest}" + "\n" +
            "\\begin{document}" + "\n" +
            "\n".join([ str(forest) for forest in self.forests ]) + "\n" +
            "\\end{document}" + "\n"
        )

class SuffixArray:
    def __init__(self, SA, LCP):
        self.SA = SA
        self.LCP = LCP
    
    def computeCommonPrefixes(self, texts):
        i,j = 0,0
        length = min([ len(t) for t in texts ])
        while(i < length):
            for k in range(1, len(texts)):
                if not texts[0][i] == texts[k][i]:
                    return j
            j += 1
            i += 1
        return j

    def fillSuffixTreePass(self, node, SA):
        if node.isLeaf():
            #node.value = SA[0]
            node.label = SA[0]
            SA = SA[1:]
        else:
            for i in range(len(node.children)):
                node.children[i], SA = self.fillSuffixTreePass(node.children[i], SA)
        return node, SA
    
    def balanceSuffixTreePass(self, node):
        if node.isLeaf():
            return node
        else:
            for i in range(len(node.children)):
                node.children[i] = self.balanceSuffixTreePass(node.children[i])
            commonPrefix = self.computeCommonPrefixes([ child.label for child in node.children ])
            node.label = node.children[0].label[:commonPrefix]
            for i in range(len(node.children)):
                node.children[i].label = node.children[i].label[commonPrefix:]
        return node
    
    def fillSuffixTree(self, root, SA):
        root, SA = self.fillSuffixTreePass(root, SA)
        root = self.balanceSuffixTreePass(root)
        return root

    def toSuffixTreePass(self, LCP):
        if len(LCP) == 0:
            return SuffixTreeNode()
        else:
            pivot = min(LCP)
            subarrays = []
            cur = []
            for v in LCP:
                if v == pivot:
                    subarrays.append(cur)
                    cur = []
                else:
                    cur.append(v)
            subarrays.append(cur)
            tree = SuffixTreeNode(children=[ self.toSuffixTreePass(arr) for arr in subarrays ])
            tree = self.fillSuffixTree(tree, self.SA)
            return tree

    def toSuffixTree(self):
        tree = SuffixTree(root=self.toSuffixTreePass(self.LCP))
        return tree
    
    def __str__(self):
        return ("SA = " + str(self.SA) + "\nLCP = " + str(self.LCP))

class DocumentWrapper:
    def __init__(self, document):
        self.document = document
    
    def dump(self, filename):
        file = open(filename, "w")
        file.write(str(self.document))
        file.close()
    
    def compile(self, filename):
        os.system(f"pdflatex {filename}")
    
    def build(self, filename = "prova"):
        self.dump(f"{filename}.tex")
        self.compile(f"{filename}.tex")

class SuffixTreeBuilder:
    def __init__(self):
        pass
    
    def build(self, text):
        return SuffixTree()

class SuffixArrayBuilder:
    def __init__(self):
        pass
    
    def computeAllSuffixes(self, text):
        return [ text[-i:] for i in range(1, len(text) + 1) ]

    def computeCommonPrefix(self, A, B):
        i,j = 0,0
        while(i < len(A) and i < len(B)):
            if A[i] == B[i]:
                j += 1
                i += 1
            else:
                break
        return j

    def build(self, text):
        SA = sorted(self.computeAllSuffixes(text))
        LCP = [ self.computeCommonPrefix(SA[i], SA[i + 1]) for i in range(len(SA) - 1) ]
        return SuffixArray(SA, LCP)

    def build2(self, texts):
        suffixes = []
        for text in texts:
            for suffix in self.computeAllSuffixes(text):
                if suffix not in suffixes:
                    suffixes.append(suffix)

        SA = sorted(suffixes)
        LCP = [ self.computeCommonPrefix(SA[i], SA[i + 1]) for i in range(len(SA) - 1) ]
        return SuffixArray(SA, LCP)

if __name__ == "__main__":
    array = SuffixArrayBuilder().build2(["bananaX", "ananasY"])
    tree = array.toSuffixTree()
    DocumentWrapper(ForestDocument(forests=[tree])).build("prova")