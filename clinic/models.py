class Service:
    def __init__(self, name, description, icon):
        self.name = name
        self.description = description
        self.icon = icon

    def __str__(self):
        return self.name


class Doctor:
    def __init__(self, name, position, category, experience, bio, education, qualifications, photo):
        self.name = name
        self.position = position
        self.category = category
        self.experience = experience
        self.bio = bio
        self.education = education
        self.qualifications = qualifications
        self.photo = photo

    def __str__(self):
        return self.name


class Promotion:
    def __init__(self, title, description, image, start_date, end_date):
        self.title = title
        self.description = description
        self.image = image
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return self.title


class Review:
    def __init__(self, author, text, photo, created_at):
        self.author = author
        self.text = text
        self.photo = photo
        self.created_at = created_at

    def __str__(self):
        return f"Отзыв от {self.author}"
