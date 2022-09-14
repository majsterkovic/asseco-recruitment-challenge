package pl.hybiak.boudingbox;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;

@Configuration
@ConfigurationProperties(prefix = "workspace.image")

public class YamlImageConfig {

    private String width;
    private String height;


    public Integer getWidth() {
        return Integer.parseInt(width);
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public Integer getHeight() {
        return Integer.parseInt(height);
    }

    public void setHeight(String height) {
        this.height = height;
    }

}

