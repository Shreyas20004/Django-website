def user_directory(instance,filename):
    return 'users_{0}/{1}'.format(instance.user.id,filename)