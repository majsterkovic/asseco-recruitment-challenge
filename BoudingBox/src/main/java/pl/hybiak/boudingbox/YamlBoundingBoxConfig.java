package pl.hybiak.boudingbox;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;

@Configuration
@ConfigurationProperties(prefix = "workspace.boundingbox")

public class YamlBoundingBoxConfig {

    private String minWidth;
    private String minHeight;


    public Integer getMinWidth() {
        return Integer.parseInt(minWidth);
    }

    public void setMinWidth(String minWidth) {
        this.minWidth = minWidth;
    }

    public Integer getMinHeight() { return Integer.parseInt(minHeight); }

    public void setMinHeight(String minHeight) {
        this.minHeight = minHeight;
    }

}

