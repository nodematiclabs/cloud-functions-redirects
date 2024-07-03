import functions_framework

from flask import redirect

REDIRECTS = {
  "/google": "https://google.com",
  "/bing": "https://bing.com",
  "/softwaresim": "https://softwaresim.com/pricing/"
}

@functions_framework.http
def redirection(request):
  path = request.path

  if path in REDIRECTS:
    return redirect(REDIRECTS[path], code=302)
  else:
    return "Not Found", 404
