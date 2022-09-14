package pl.hybiak.boudingbox;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;
@Service
public class BoundingboxService {

    @Autowired
    private YamlImageConfig yamlImage;
    @Autowired
    private YamlBoundingBoxConfig yamlBoundingBox;
    private final HashMap<Integer, BoundingBox> boxes = new HashMap<>();

    private boolean checkXY(int x1, int y1, int x2, int y2)
    {
        if(x2 - x1 < yamlBoundingBox.getMinWidth())
        {
            return false;
        }
        else if(y2 - y1 < yamlBoundingBox.getMinHeight())
        {
            return false;
        }
        else if(x1 * y1 < 0)
        {
            return false;
        }
        else if(x2 > yamlImage.getWidth())
        {
            return false;
        }
        else return y2 <= yamlImage.getHeight();
    }

    public boolean add(BoundingBox box) {
        if(checkXY(box.getX1(), box.getY1(), box.getX2(), box.getY2()))
        {
            boxes.put(box.hashCode(), box);
            return true;
        }
        else
        {
            return false;
        }
    }

    public boolean remove(Integer id){
        if (boxes.containsKey(id)) {
            boxes.remove(id);
            return true;
        } else {
            return false;
        }
    }

    public BoundingBox get(Integer id){
        return boxes.getOrDefault(id, null);
    }

    public boolean edit(EditBoundingBox box) {
        Integer id = box.getId();

        if (boxes.containsKey(id)) {
            BoundingBox box_to_edit = boxes.get(id);

            box_to_edit.setX1(box.getX1());
            box_to_edit.setY1(box.getY1());
            box_to_edit.setX2(box.getX2());
            box_to_edit.setY2(box.getY2());
            boxes.remove(id);
            boxes.put(id, box_to_edit);
            return true;
        } else {
            return false;
        }
    }

    public HashMap<Integer, BoundingBox> getAll(){
        return boxes;
    }
}
