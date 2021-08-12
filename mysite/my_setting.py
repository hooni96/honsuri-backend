DATABASES = {
	'default' : {
        # "ENGINE": "django.db.backends.sqlite3",
        # "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'honsuri', # 데이터베이스명
		'USER': 'root', # 데이터베이스 접속 계정명
		'PASSWORD': 'dainlinda!0325', # 데이터베이스 접속 패스워드
		'HOST': 'localhost', # 데이터베이스 주소
		'PORT': '3306', # 포트 번호
		'OPTIONS': {'charset': 'utf8mb4'},
		'TEST': {
			'CHARSET': 'utf8mb4',
			'COLLATION': 'utf8_general_ci'
		}
	}
}

SECRET = {
        'secret':'django-insecure-491n)$8vzwjqq95zm5d002lt3m9z+z^wgwa(t@k01qyan)+t61',
}