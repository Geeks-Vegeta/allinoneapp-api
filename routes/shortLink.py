from flask import Flask, request
from flask_restful import Resource
import pyshorteners


class ShortLink(Resource):
    def post(self):

        s = pyshorteners.Shortener()

        mode = request.args.get('mode')
        link = request.args.get('link')

        out_link = s.chilpit.short(link)

        if mode=="tinyurl":
            out_link = s.tinyurl.short(link)
            return {"url": str(out_link)}


        if mode=="osdb":
            out_link = s.osdb.short(link)
            return {"url": str(out_link)}


        if mode=="clckru":
            out_link = s.clckru.short(link)
            return {"url": str(out_link)}


        if mode=="chilpit":
            out_link = s.chilpit.short(link)
            return {"url": str(out_link)}

        
        if mode=="dagd":
            out_link = s.dagd.short(link)
            return {"url": str(out_link)}


        return {"message": out_link}