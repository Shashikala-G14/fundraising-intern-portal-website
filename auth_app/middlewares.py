from django.shortcuts import redirect
 # ********** Authenticated users only **********
def auth(view_function):
  def wrapped_view(request,*args,**kwargs):
    if request.user.is_authenticated==False:
      return redirect('login')
    return view_function(request,*args,**kwargs)
  return wrapped_view

 # ********** Guest users**********
def guest(view_function):
  def wrapped_view(request,*args,**kwargs):
    if request.user.is_authenticated:
      return redirect('dashboard')
    return view_function(request,*args,**kwargs)
  return wrapped_view