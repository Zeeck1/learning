from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Course, Lession, UserCourseLink, QuizQuestion, QuizResult

# Custom Admin class for Course with search functionality
class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name', 'author']  # Search by course name and author
    list_display = ['name', 'author', 'created_at']  # Display course name, author, and created_at
    list_filter = ['author', 'created_at']  # Optional: Add filters for easier navigation

# Custom Admin class for Lession with search functionality
class LessionAdmin(admin.ModelAdmin):
    search_fields = ['name', 'course__name']  # Search by lession name and course name
    list_display = ['name', 'course', 'duration']  # Display key information in the list view
    list_filter = ['course']  # Optional: Filter by course

# Custom Admin class for QuizQuestion with search functionality
class QuizQuestionAdmin(admin.ModelAdmin):
    search_fields = ['course__name', 'question', 'option1', 'option2', 'option3', 'option4']  # Search by these fields
    list_display = ['course', 'question', 'answer']  # Display key information in the list view
    list_filter = ['course']  # Optional: Filter by course

# Custom Admin class for UserCourseLink with search functionality
class UserCourseLinkAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'course__name']  # Search by user username and course name
    list_display = ['user', 'course']  # Display user and course
    list_filter = ['user', 'course']  # Optional: Add filters for easier navigation

# Register all custom admin classes
admin.site.register(Course, CourseAdmin)  # Register Course with custom admin
admin.site.register(Lession, LessionAdmin)  # Register Lession with custom admin
admin.site.register(UserCourseLink, UserCourseLinkAdmin)  # Register UserCourseLink with custom admin
admin.site.register(QuizQuestion, QuizQuestionAdmin)  # Register QuizQuestion with custom admin

# Custom Admin class for QuizResult
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'result', 'display_selected_options']  # Display key information
    list_filter = ['course', 'user']  # Allow filtering by course and user
    search_fields = ['user__username', 'course__name', 'result']  # Enable searching by these fields
    
    # Custom method to show a snippet of 'selected_options' in the admin list view
    def display_selected_options(self, obj):
        return obj.selected_options[:50]  # Show the first 50 characters to keep it concise

    display_selected_options.short_description = 'Selected Options'  # Custom column name

admin.site.register(QuizResult, QuizResultAdmin)  # Register QuizResult with custom admin

# Custom configuration for UserAdmin
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'date_joined', 'get_enrolled_courses', 'get_user_results', 'display_user_options']  # Display user info and other custom fields

    def get_enrolled_courses(self, obj):
        enrolled_courses = UserCourseLink.objects.filter(user=obj).values_list("course__name", flat=True)
        return ", ".join(enrolled_courses)

    def get_user_results(self, obj):
        user_results = QuizResult.objects.filter(user=obj).values_list("result", flat=True)
        return ", ".join(user_results)

    def display_user_options(self, obj):
        user_options = QuizResult.objects.filter(user=obj).values_list("selected_options", flat=True)
        return ", ".join(user_options)

admin.site.unregister(User)  # Unregister default UserAdmin
admin.site.register(User, CustomUserAdmin)  # Register the custom UserAdmin

# Set custom site header for the admin site
admin.site.site_header = "C.K E-Learning System Admin Site"  # Custom admin site header
admin.site.site_title = "C.K E-Learning System Admin Site"
