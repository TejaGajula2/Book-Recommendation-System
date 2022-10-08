class CustomLoginView(LoginView): 
 template_name = "user/login.html" 
 redirect_authenticated_user = True

class UserView(AdminRequiredJsonMixin, View):
   def post(self, request, id, *args, **kwargs): 
   	try:
       user_instance = User.objects.get(id=id) form = 
       UserForm(request.POST, instance=user_instance) if 
       form.is_valid(): form.save()
       return JsonResponse({"message": ["success"]})
     return JsonResponse(form.errors, status=400)
    except Exception as e: return JsonResponse({"error": 
    	[e.__str__()]}, status=400)

class SignUpView(FormView, CreateView):
   form_class = SignUpForm 
   template_name = "user/signup.html" 
   success_url = "/home"
