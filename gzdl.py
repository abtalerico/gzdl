#!/usr/bin/env python3
import sys
from gzdl.main import GzdlApp

if __name__ == '__main__':
    app = GzdlApp(application_id="com.example.GtkApplication")
    app.run(sys.argv)
