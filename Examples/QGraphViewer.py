#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Author: Saifeddine ALOUI
Description:
A simple graphviz graphs viewer
"""
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout
import sys
import os
sys.path.insert(1,os.path.dirname(__file__)+"/..")
print(sys.path)
from QGraphViz.QGraphViz import QGraphViz
from QGraphViz.DotParser import Graph
from QGraphViz.Engines import Dot
if __name__ == "__main__":
    app = QApplication(sys.argv)
    qgv = QGraphViz()
    qgv.new(Dot(Graph()))
    n1 = qgv.addNode("Node1", label="N1")
    n2 = qgv.addNode("Node2", label="N2")
    n3 = qgv.addNode("Node3", label="N3")
    qgv.addEdge(n1, n2)
    qgv.build()
    w = QMainWindow()
    w.setWindowTitle('Simple')
    wi=QWidget()
    wi.setLayout(QVBoxLayout())
    w.setCentralWidget(wi)
    wi.layout().addWidget(qgv)

    w.showMaximized()
    
    sys.exit(app.exec_())