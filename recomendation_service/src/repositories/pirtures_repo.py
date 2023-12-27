from uuid import UUID

from src.domain.picture import Picture


class PicturesRepositoryList:
    pictures = []

    def get_picture_by_id(self, id: UUID) -> Picture:
        print(id)
        return next((pic for pic in self.pictures if pic.id == id), None)

    def select_all(self) -> list[Picture]:
        return self.pictures

    def select_by_name(self, name) -> Picture:
        return next((pic for pic in self.pictures if pic.name.lower() == name.lower()), None)

    def select_by_writer_name(self, writer_name) -> list[Picture]:
        return [pic for pic in self.pictures if pic.full_name == writer_name]

    def create_picture(self, pic: Picture) -> Picture:
        self.pictures.append(pic)
        return pic

    def update_picture(self, id: UUID, pic: Picture) -> Picture:
        indx = next((e for e, pic in enumerate(self.pictures) if pic.id == id), -1)
        if indx == -1:
            return None
        else:
            self.pictures[indx] = pic
            return self.pictures[indx]

    def delete_picture(self, id: UUID):
        indx = next((e for e, pic in enumerate(self.pictures) if pic.id == id), -1)
        if indx != -1:
            del self.pictures[indx]
