import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;
import java.util.regex.*;
import java.util.zip.*;
import com.google.gson.*;
import com.mojang.serialization.JsonOps;
import net.minecraft.locale.Language;
import net.minecraft.network.chat.*;
import net.minecraft.server.packs.metadata.pack.PackMetadataSection;
import net.minecraft.util.FormattedCharSequence;

public class CheckFrenchPack {
    public static void main(String[] args) throws Exception {
        net.minecraft.SharedConstants.tryDetectVersion();
        net.minecraft.server.Bootstrap.bootStrap();
        var values = new HashMap<String, String>();
        try (var pack = new ZipFile(args[0])) {
            var metadata = JsonParser.parseString(new String(pack.getInputStream(pack.getEntry("pack.mcmeta")).readAllBytes(), StandardCharsets.UTF_8)).getAsJsonObject();
            var decoded = PackMetadataSection.CLIENT_TYPE.codec().parse(JsonOps.INSTANCE, metadata.get("pack")).getOrThrow();
            System.out.println("MC26_2_PACK_METADATA_OK " + decoded.supportedFormats());
            try (var stream = pack.getInputStream(pack.getEntry("assets/openpartiesandclaims/lang/fr_fr.json"))) {
                Language.loadFromJson(stream, values::put);
            }
        }
        Language old = Language.getInstance();
        Language.inject(new Language() {
            public String getOrDefault(String k, String fallback) { return values.getOrDefault(k, old.getOrDefault(k, fallback)); }
            public boolean has(String k) { return values.containsKey(k) || old.has(k); }
            public boolean isDefaultRightToLeft() { return false; }
            public FormattedCharSequence getVisualOrder(FormattedText text) { return FormattedCharSequence.forward(text.getString(), Style.EMPTY); }
        });
        int checked = 0;
        for (var entry : values.entrySet()) {
            Matcher m = Pattern.compile("%(\\d+)\\$s").matcher(entry.getValue());
            int count = 0;
            while (m.find()) count = Math.max(count, Integer.parseInt(m.group(1)));
            Object[] arguments = new Object[count];
            for (int i = 0; i < count; i++) arguments[i] = "ARG" + (i + 1);
            String rendered = Component.translatable(entry.getKey(), arguments).getString();
            if (rendered.equals(entry.getKey()) || rendered.matches("(?s).*%\\d+\\$[sd].*"))
                throw new AssertionError("Unresolved text: " + entry.getKey());
            checked++;
        }
        if (!Component.translatable("gui.xaero_pac_config_option_sub_inherited").getString().equals("Hérité")) throw new AssertionError("inheritance");
        if (!Component.translatable("gui.xaero_pac_ui_on").getString().equals("OUI")) throw new AssertionError("on");
        if (!Component.translatable("gui.xaero_pac_ui_off").getString().equals("NON")) throw new AssertionError("off");
        if (!Component.translatable("gui.xaero_pac_player_config_playerConfig.claims.protection.exceptions.groups.block.interact", "Chests").getString().equals("Utiliser (Chests)")) throw new AssertionError("literal group IDs");
        System.out.println("MC26_2_LANGUAGE_FORMAT_OK " + checked + " entries");
    }
}
